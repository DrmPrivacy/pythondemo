from PyInstaller.__main__ import run
if __name__ == '__main__':
    opts = [r'C:\Users\think\PycharmProjects\untitled1\winform.py',\
            '-F','-w',r'--distpath=C:\Users\think\PycharmProjects\untitled1',\
            r'--workpath=C:\Users\think\PycharmProjects\untitled1',\
            r'--specpath=C:\Users\think\PycharmProjects\untitled1',\
            r'--upx-dir','upx393w']
    run(opts)