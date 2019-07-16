import platform
import sys

if platform.system() == 'Windows':
    import mode_creator_windows
elif platform.system() == 'Linux':
    import mode_creator_linux
else:
    sys.exit('Error: unsupported OS: %s' % platform.system())