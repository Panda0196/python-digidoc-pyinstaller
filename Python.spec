# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['Python.py'],
             pathex=['C:\\Example Files3äõüöÄÕÜÖ'],
             binaries=[],
             datas=[('TEST.asice', '.'), ('TEST2.asice', '.'), ('digidoc-tool.exe', '.'), ('digidocpp.dll', '.'), ('libcrypto-3-x64.dll', '.'), ('libssl-3-x64.dll', '.'), ('Xalan-C_1_12.dll', '.'), ('XalanMessages_1_12.dll', '.'), ('xerces-c_3_2.dll', '.'), ('xsec_2_0.dll', '.'), ('zlib1.dll', '.')], 
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

a.datas += Tree('./schema', prefix='schema')

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='Python',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
