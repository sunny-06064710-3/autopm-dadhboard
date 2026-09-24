"""Validate this delivery documentation; does not access or certify Airtable."""
from pathlib import Path
import json
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
HUB = ROOT / 'docs/delivery'


def main():
    docs = [ROOT / name for name in ('README.md', 'AGENTS.md', 'docs/README.md',
            'collaboration/README.md', 'docs/archive/README.md')]
    docs += sorted(HUB.glob('*.md'))
    links = 0
    for doc in docs:
        body = doc.read_text(encoding='utf-8')
        for target in re.findall(r'\[[^\]]*\]\(([^\n)]+)\)', body):
            target = target.strip('<>')
            if urlsplit(target).scheme or target.startswith('#'):
                continue
            path = (doc.parent / unquote(target.split('#')[0])).resolve()
            assert path.is_relative_to(ROOT) and path.exists(), (doc.name, target)
            links += 1
    clean = json.loads((HUB / 'cleanup-manifest.json').read_text(encoding='utf-8'))
    assert len(clean['removed_files']) == 47
    for item in clean['removed_files']:
        path = (ROOT / item['path']).resolve()
        assert path.is_relative_to(ROOT) and not path.exists(), item['path']
        assert re.fullmatch('[0-9a-f]{64}', item['sha256'])
    evidence = json.loads((HUB / 'evidence-manifest.json').read_text(encoding='utf-8'))
    assert evidence['raw_evidence_uploaded'] is False
    for path in HUB.glob('*.md'):
        # Reject accidental raw Airtable identities or actual mailbox addresses.
        content = path.read_text(encoding='utf-8')
        assert not re.search(r'\b(?:rec|fld|tbl|app|wfl|pag)[A-Za-z0-9]{14}\b', content), path.name
        assert not re.search(r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}', content), path.name
    print(f'PASS: {len(docs)} documents, {links} local links, 47 removals; no Airtable writes')


if __name__ == '__main__':
    main()
