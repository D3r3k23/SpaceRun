
from distutils.core import setup
import py2exe, glob

opts = {
    "py2exe": {
        'includes': [
            'src\\'
        ]
    }
}

setup(
    windows = ['Main.py'],
    options = opts,
    data_files = [
        ('images', glob.glob('\\resources\\images\\*.png')
                 + glob.glob('\\resources\\images\\*.jpg')),
        ('sounds', glob.glob('\\resources\\sounds\\*.mp3')),
        ('music' , glob.glob('\\resources\\music\\*.mp3'))
    ]
)