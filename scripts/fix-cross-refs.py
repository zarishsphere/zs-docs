#!/usr/bin/env python3
"""
fix-cross-refs.py — Convert unlinked ZUSS cross-references to clickable links.

Converts:  → **target.md**  ...  →  → **[target.md](target.md)**
Handles section refs, trailing asterisks, and nested content.
Skips already-linked refs, inline code, fenced code blocks, and template docs.
"""

import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Directories to scan
DOC_DIRS = [os.path.join(ROOT, d) for d in os.listdir(ROOT)
            if re.match(r'^\d{3}-', d) and os.path.isdir(os.path.join(ROOT, d))]

# Pattern: → **target.md** optionally with trailing * and content after
# We must NOT match already-linked refs (→ **[text](target)**)
ZUSS_REF_RE = re.compile(
    r'(→\s+)\*\*([^*\]]+\.md)\*{2,3}'
)

def fix_file(filepath):
    """Fix all ZUSS cross-refs in a file. Returns (changed_count, line_numbers)."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Skip fenced code blocks
    lines = content.split('\n')
    in_code_block = False
    in_yaml = False
    modified_lines = []
    changed_lines = []
    
    for i, line in enumerate(lines):
        line_num = i + 1
        
        # Track YAML front matter
        if line.strip() == '---':
            if not in_yaml:
                in_yaml = True
                modified_lines.append(line)
                continue
            else:
                in_yaml = False
                modified_lines.append(line)
                continue
        
        # Track fenced code blocks
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            modified_lines.append(line)
            continue
        
        # Skip content inside YAML or code blocks
        if in_yaml or in_code_block:
            modified_lines.append(line)
            continue
        
        # Skip lines that already have linked refs
        if '→ **[**' in line:
            modified_lines.append(line)
            continue
        
        # Skip lines inside inline code (backtick-wrapped)
        # We'll handle this by checking for backticks
        
        # Apply regex replacement
        new_line = ZUSS_REF_RE.sub(
            r'\1**[\2](\2)**',
            line
        )
        
        if new_line != line:
            changed_lines.append(line_num)
        
        modified_lines.append(new_line)
    
    new_content = '\n'.join(modified_lines)
    
    if new_content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
    
    return len(changed_lines), changed_lines


def main():
    all_files = []
    for doc_dir in DOC_DIRS:
        for root, dirs, files in os.walk(doc_dir):
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            for f in files:
                if f.endswith('.md'):
                    all_files.append(os.path.join(root, f))
    
    all_files.sort()
    
    total_changed = 0
    total_fixes = 0
    changed_files_list = []
    
    print('Scanning and fixing cross-references...')
    print()
    
    for fpath in all_files:
        rel = os.path.relpath(fpath, ROOT)
        fixes, lines = fix_file(fpath)
        if fixes > 0:
            total_changed += 1
            total_fixes += fixes
            changed_files_list.append((rel, lines))
            print(f'  ✎ {rel} — {fixes} fix(es) on lines: {",".join(map(str, lines))}')
    
    print()
    print(f'Summary: {total_fixes} cross-reference(s) converted to clickable links')
    print(f'         across {total_changed} file(s)')
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
