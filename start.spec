# -*- mode: python ; coding: utf-8 -*-


block_cipher = None
SETUP_DIR = 'E:\\12313123\\pythonTest\\HelloWorld\\static\\app\\'

a = Analysis(
    ['start.py',
    SETUP_DIR + 'response.py',
    SETUP_DIR + 'mongoClient.py',
    ],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['flask','nb_log','pymongo'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='start',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='start',
)
