#!E:\Projects\music-server\env\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'mutagen==1.44.0','console_scripts','mutagen-inspect'
__requires__ = 'mutagen==1.44.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('mutagen==1.44.0', 'console_scripts', 'mutagen-inspect')()
    )
