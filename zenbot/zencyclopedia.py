from collections import defaultdict
import re
from this import d, s

_zen = ''.join(d.get(c, c) for c in s)
_zen_lines = _zen.splitlines()[2:]
index = defaultdict(set)
for line in _zen_lines:
    for word in line.split():
        index[re.search(r'\w*', word.lower()).group()].add(line)
