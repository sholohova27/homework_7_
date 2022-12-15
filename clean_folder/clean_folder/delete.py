import os
from pathlib import Path


def delete(path_):
    p = Path(path_)
    for i in p.iterdir():
        if i.is_dir() and i.name not in \
                ('Images', 'Video', 'Docs', 'Audio', 'Archives', 'Requests', 'Reports', 'Others'):
            try:
                os.rmdir(os.path.join(path_, i.name))
            except:
                pass
    return i.name
