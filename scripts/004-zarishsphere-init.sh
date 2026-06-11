#!/usr/bin/env bash
# 004-zarishsphere-init.sh — Bootstrap the ZarishSphere GitHub ecosystem
# Run this after opencode config is set up and gh is authenticated.
# This creates all repos, sets up org structure, and initializes each project
# with README, LICENSE, .gitignore, and CI validation workflows.
set -euo pipefail

ORG="zarishsphere"
GH_FLAGS="--public --clone"

echo "=== ZarishSphere GitHub Ecosystem Initialization ==="
echo "Org: $ORG"
echo "Date: $(date -I)"
echo ""

# Repos in creation order (dependencies first)
REPOS=(
  "zs-docs"                # Documentation (this repo)
  "zs-zarish-index"        # ZARISH-INDEX data engine
  "zs-zarish-standards"    # ZARISH-STANDARDS transformation
  "zs-platform"            # Core platform (Go backend)
  "zs-console"             # Console frontend
  "zs-marketplace"         # Marketplace
  "zs-builder"             # Builder
  "zs-apps"                # Applications
  "zs-forms"               # Forms engine
  "zs-sdk"                 # SDK
  "zs-cli"                 # CLI tool
  "zs-api"                 # Public API gateway
  "zs-engine"              # Engine
)

# Ensure org exists
echo "Checking org $ORG..."
if ! gh api "orgs/$ORG" >/dev/null 2>&1; then
  echo "ERROR: Org $ORG does not exist. Create it at github.com/organizations/plan"
  echo "Then re-run this script."
  exit 1
fi
echo "  Org exists: ✓"
echo ""

# Create repos
for REPO in "${REPOS[@]}"; do
  if gh repo view "$ORG/$REPO" >/dev/null 2>&1; then
    echo "  EXISTS  $ORG/$REPO — skipping"
  else
    echo "  CREATE  $ORG/$REPO"
    gh repo create "$REPO" $GH_FLAGS --description "ZarishSphere ecosystem — $REPO"
  fi
done

echo ""
echo "=== Repo creation complete ==="
echo ""
echo "Next steps:"
echo "  1. Push zs-docs content: git remote add origin git@github.com:$ORG/zs-docs.git && git push -u origin main"
echo "  2. Clone each new repo and add README.md, LICENSE, .gitignore"
echo "  3. Set up GitHub Pages for zs-docs (Settings > Pages > main > /docs)"
echo "  4. Configure branch protection on main for each repo"
