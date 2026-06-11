#!/usr/bin/env node
const { spawn } = require("child_process");

const TOOLS = [
  {
    name: "create_repository",
    description: "Create a new GitHub repository under the zarishsphere org",
    inputSchema: {
      type: "object",
      properties: {
        name: { type: "string", description: "Repository name (e.g., zs-platform)" },
        description: { type: "string", description: "Short description" },
        visibility: { type: "string", enum: ["public", "private"], default: "public" }
      },
      required: ["name"]
    }
  },
  {
    name: "list_repositories",
    description: "List repositories in the zarishsphere org or for the user",
    inputSchema: {
      type: "object",
      properties: {
        owner: { type: "string", description: "Owner (org or user)", default: "zarishsphere" },
        limit: { type: "number", default: 30 }
      }
    }
  },
  {
    name: "create_issue",
    description: "Create a GitHub issue in a repository",
    inputSchema: {
      type: "object",
      properties: {
        repo: { type: "string", description: "Repository name (e.g., zs-docs)" },
        title: { type: "string" },
        body: { type: "string" },
        labels: { type: "array", items: { type: "string" } }
      },
      required: ["repo", "title", "body"]
    }
  },
  {
    name: "create_pull_request",
    description: "Create a pull request",
    inputSchema: {
      type: "object",
      properties: {
        repo: { type: "string" },
        title: { type: "string" },
        body: { type: "string" },
        head: { type: "string", description: "Source branch" },
        base: { type: "string", default: "main" }
      },
      required: ["repo", "title", "head"]
    }
  },
  {
    name: "list_issues",
    description: "List issues in a repository",
    inputSchema: {
      type: "object",
      properties: {
        repo: { type: "string" },
        state: { type: "string", enum: ["open", "closed", "all"], default: "open" },
        limit: { type: "number", default: 20 }
      },
      required: ["repo"]
    }
  },
  {
    name: "run_workflow",
    description: "Trigger a GitHub Actions workflow",
    inputSchema: {
      type: "object",
      properties: {
        repo: { type: "string" },
        workflow: { type: "string", description: "Workflow filename or ID" },
        ref: { type: "string", default: "main", description: "Branch to run on" }
      },
      required: ["repo", "workflow"]
    }
  },
  {
    name: "list_workflows",
    description: "List GitHub Actions workflows in a repo",
    inputSchema: {
      type: "object",
      properties: {
        repo: { type: "string" }
      },
      required: ["repo"]
    }
  }
];

function gh(args) {
  return new Promise((resolve, reject) => {
    const proc = spawn("gh", args, { stdio: ["pipe", "pipe", "pipe"] });
    let stdout = "", stderr = "";
    proc.stdout.on("data", (d) => stdout += d);
    proc.stderr.on("data", (d) => stderr += d);
    proc.on("close", (code) => {
      if (code === 0) resolve(stdout.trim());
      else reject(new Error(stderr.trim() || `gh exited with code ${code}`));
    });
  });
}

async function handleToolCall(name, args) {
  switch (name) {
    case "create_repository":
      return await gh([
        "repo", "create", args.name,
        "--description", args.description || "",
        "--" + (args.visibility || "public"),
        "--clone"
      ]);
    case "list_repositories":
      return await gh(["repo", "list", args.owner || "zarishsphere",
        "--limit", String(args.limit || 30), "--json", "name,description,visibility,updatedAt"]);
    case "create_issue":
      return await gh(["issue", "create",
        "--repo", `zarishsphere/${args.repo}`,
        "--title", args.title,
        "--body", args.body,
        ...(args.labels ? ["--label", args.labels.join(",")] : [])]);
    case "create_pull_request":
      return await gh(["pr", "create",
        "--repo", `zarishsphere/${args.repo}`,
        "--title", args.title,
        "--body", args.body || "",
        "--head", args.head,
        "--base", args.base || "main"]);
    case "list_issues":
      return await gh(["issue", "list",
        "--repo", `zarishsphere/${args.repo}`,
        "--state", args.state || "open",
        "--limit", String(args.limit || 20),
        "--json", "number,title,state,labels,updatedAt"]);
    case "run_workflow":
      return await gh(["workflow", "run", args.workflow,
        "--repo", `zarishsphere/${args.repo}`,
        "--ref", args.ref || "main"]);
    case "list_workflows":
      return await gh(["workflow", "list",
        "--repo", `zarishsphere/${args.repo}`,
        "--json", "id,name,state"]);
    default:
      throw new Error(`Unknown tool: ${name}`);
  }
}

const buf = [];
process.stdin.on("data", (chunk) => {
  buf.push(chunk.toString());
  const text = buf.join("");
  const parts = text.split("\n");
  buf.length = 0;
  for (let i = 0; i < parts.length - 1; i++) {
    const line = parts[i].trim();
    if (!line) continue;
    try {
      const msg = JSON.parse(line);
      handleMessage(msg);
    } catch (e) {
      // skip malformed
    }
  }
  if (parts[parts.length - 1]) buf.push(parts[parts.length - 1]);
});

function respond(msg) {
  process.stdout.write(JSON.stringify(msg) + "\n");
}

async function handleMessage(msg) {
  const id = msg.id;
  switch (msg.method) {
    case "initialize":
      respond({ id, result: { protocolVersion: "0.1.0", capabilities: { tools: {} } } });
      break;
    case "tools/list":
      respond({ id, result: { tools: TOOLS } });
      break;
    case "tools/call":
      try {
        const result = await handleToolCall(msg.params.name, msg.params.arguments || {});
        respond({ id, result: { content: [{ type: "text", text: String(result) }] } });
      } catch (err) {
        respond({ id, error: { code: -32000, message: err.message } });
      }
      break;
    default:
      respond({ id, error: { code: -32601, message: `Method not found: ${msg.method}` } });
  }
}
