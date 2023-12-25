# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['..\\main.py'],
    pathex=[],
    binaries=[],
    datas=[('D:\\projects_work\\python_apps\\PySide6_calculator\\imgs\\', 'imgs\\'), ('D:\\projects_work\\python_apps\\PySide6_calculator\\src\\', 'src\\'), ('D:\\projects_work\\python_apps\\PySide6_calculator\\style\\', 'style\\')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Sapucaia Calculadora',
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
    icon=['D:\\projects_work\\python_apps\\PySide6_calculator\\imgs\\kerismaker_icon.png'],
)
