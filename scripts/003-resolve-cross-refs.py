#!/usr/bin/env python3
"""
003-resolve-cross-refs.py — Cross-Reference Validator (v3)

Fast Python implementation. Scans all .md files for cross-references
and validates that target files exist. Handles:
  - Markdown links: [text](target.md)
  - ZUSS cross-refs: → **target.md**
  - Wikilinks: [[target.md]]

Usage: python3 scripts/003-resolve-cross-refs.py
Returns: exit 0 if all resolve, 1 if any broken
"""

import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Skip these directories
SKIP_DIRS = {'scripts', '.git', '.opencode', 'node_modules'}

# Patterns for template/example filenames to skip
TEMPLATE_PATTERNS = re.compile(
    r'filename|example|template|your-|old-name|new-name', re.I
)

# Patterns to extract targets from different reference styles
MARKDOWN_LINK_RE = re.compile(r'\]\(([^)]+\.md[^)]*)\)')
ZUSS_REF_RE = re.compile(r'→\s+\*\*([^*]+\.md[^*]*)\*\*')
WIKI_RE = re.compile(r'\[\[([^\]]+\.md[^\]]*)\]\]')


def collect_md_files():
    """Collect all .md files under doc folders (001-010)."""
    files = []
    for d in sorted(glob.glob(os.path.join(ROOT, '00[0-9]-*/'))):
        for root, dirs, fnames in os.walk(d):
            # Skip excluded dirs
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            for fn in fnames:
                if fn.endswith('.md'):
                    files.append(os.path.join(root, fn))
    return sorted(files)


def find_targets(content, regex):
    """Find all reference targets in content using the given regex."""
    targets = []
    for match in regex.finditer(content):
        target = match.group(1).strip()
        targets.append(target)
    return targets


def is_template(name):
    """Check if a target name looks like a template/example."""
    # Remove leading ../ path components
    base = name.lstrip('../')
    base = os.path.basename(base)
    return bool(TEMPLATE_PATTERNS.search(base))


def is_cross_repo(target):
    """Check if target is a cross-repo reference (zs-*)."""
    return target.startswith('zs-')


def resolve_target(source_file, target):
    """Try to resolve a target path relative to source file."""
    dirpath = os.path.dirname(source_file)

    # Strip anchor (#... or §...)
    file_target = re.split(r'[#§]', target)[0].strip()

    if not file_target:
        return None, 'empty'

    # Skip external URLs
    if file_target.startswith(('http://', 'https://')):
        return None, 'external'

    # Skip absolute paths
    if file_target.startswith('/'):
        return None, 'absolute'

    # Skip cross-repo references
    if is_cross_repo(file_target):
        return None, 'cross-repo'

    # Skip template/example patterns
    if is_template(file_target):
        return None, 'template'

    # Try relative to source file
    resolved = os.path.normpath(os.path.join(dirpath, file_target))
    if os.path.isfile(resolved):
        return resolved, 'ok'

    # Try root-relative
    root_resolved = os.path.normpath(os.path.join(ROOT, file_target))
    if os.path.isfile(root_resolved):
        return root_resolved, 'root-relative'

    return None, 'not-found'


def main():
    files = collect_md_files()
    print(f'Scanning {len(files)} files for cross-references...')
    print()

    passed = 0
    failed = 0
    skipped = {'external': 0, 'absolute': 0, 'cross-repo': 0, 'template': 0}

    # Read all files into memory
    file_contents = {}
    for f in files:
        try:
            with open(f, 'r', encoding='utf-8') as fh:
                file_contents[f] = fh.read()
        except Exception as e:
            print(f'  WARN: Cannot read {f}: {e}')

    basenames = {f: os.path.basename(f) for f in files}

    # Section 1: Markdown link references
    print('\033[0;36m═══ 1. Markdown link references ═══\033[0m')
    for f in files:
        content = file_contents.get(f, '')
        if not content:
            continue
        for target in find_targets(content, MARKDOWN_LINK_RE):
            result, status = resolve_target(f, target)
            bname = basenames[f]
            if status == 'ok':
                passed += 1
                print(f'  \033[0;32m✓\033[0m {bname} → {target}')
            elif status == 'root-relative':
                passed += 1
                print(f'  \033[0;32m✓\033[0m {bname} → {target} (root-relative)')
            elif status in skipped:
                skipped[status] += 1
            else:
                failed += 1
                print(f'  \033[0;31m✗\033[0m {bname} → {target} (not found)')

    # Section 2: ZUSS cross-refs
    print('\n\033[0;36m═══ 2. ZUSS cross-reference notation (→ **target.md**) ═══\033[0m')
    for f in files:
        content = file_contents.get(f, '')
        if not content:
            continue
        for target in find_targets(content, ZUSS_REF_RE):
            # Skip if it's a markdown link inside bold (handled by section 1)
            if '(' in target or target.startswith('['):
                continue
            result, status = resolve_target(f, target)
            bname = basenames[f]
            if status == 'ok':
                passed += 1
                print(f'  \033[0;32m✓\033[0m {bname} → {target}')
            elif status == 'root-relative':
                passed += 1
                print(f'  \033[0;32m✓\033[0m {bname} → {target} (root-relative)')
            elif status in skipped:
                skipped[status] += 1
            else:
                failed += 1
                print(f'  \033[0;31m✗\033[0m {bname} → {target} (not found)')

    # Section 3: Wikilinks
    wiki_count = sum(1 for f in files for _ in find_targets(file_contents.get(f, ''), WIKI_RE))
    if wiki_count > 0:
        print('\n\033[0;36m═══ 3. Wikilink-style cross-references ([[target.md]]) ═══\033[0m')
        for f in files:
            content = file_contents.get(f, '')
            if not content:
                continue
            for target in find_targets(content, WIKI_RE):
                result, status = resolve_target(f, target)
                bname = basenames[f]
                if status == 'ok':
                    passed += 1
                    print(f'  \033[0;32m✓\033[0m {bname} → {target}')
                elif status == 'root-relative':
                    passed += 1
                    print(f'  \033[0;32m✓\033[0m {bname} → {target} (root-relative)')
                elif status in skipped:
                    skipped[status] += 1
                else:
                    failed += 1
                    print(f'  \033[0;31m✗\033[0m {bname} → {target} (not found)')

    # Summary
    total_skipped = sum(skipped.values())
    print()
    print('\033[0;36m════════════════════════════════════════\033[0m')
    print('\033[0;36m  Cross-reference summary\033[0m')
    print('\033[0;36m════════════════════════════════════════\033[0m')
    print(f'  \033[0;32mResolved:\033[0m {passed}')
    print(f'  \033[0;31mBroken:\033[0m {failed}')
    print(f'  \033[1;33mSkipped:\033[0m {total_skipped}')
    if skipped.get('external'):
        print(f'         (external: {skipped["external"]})')
    if skipped.get('absolute'):
        print(f'         (absolute: {skipped["absolute"]})')
    if skipped.get('cross-repo'):
        print(f'         (cross-repo: {skipped["cross-repo"]})')
    if skipped.get('template'):
        print(f'         (template: {skipped["template"]})')
    print()

    if failed == 0:
        print('\033[0;32m✓ All cross-references resolve.\033[0m')
    else:
        print(f'\033[0;31m✗ {failed} broken cross-references found. Review above.\033[0m')

    return 0 if failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
