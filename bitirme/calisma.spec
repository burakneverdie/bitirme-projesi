# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['calisma.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/burakk/Desktop/kubiPyhton2/kubiPyhton2/yapayzekaresmi.jpg', '.'), ('C:/Users/burakk/PycharmProjects/bitirme-projesi/model/sentiment_model.keras', '.'), ('C:/Users/burakk/Desktop/kubiPyhton2/kubiPyhton2/tokenizer.pickle', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='calisma',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
