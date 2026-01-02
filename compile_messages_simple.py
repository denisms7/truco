#!/usr/bin/env python
"""
Script simples para compilar mensagens de traducao usando polib.
"""
import sys
from pathlib import Path

try:
    import polib
except ImportError:
    print("Erro: polib nao instalado. Instale com: pip install polib")
    sys.exit(1)

BASE_DIR = Path(__file__).resolve().parent
locale_dir = BASE_DIR / 'locale'

print("Compilando mensagens de traducao...")

# Compila o arquivo de espanhol
po_file = locale_dir / 'es' / 'LC_MESSAGES' / 'django.po'
mo_file = locale_dir / 'es' / 'LC_MESSAGES' / 'django.mo'

if po_file.exists():
    try:
        po = polib.pofile(str(po_file))
        po.save_as_mofile(str(mo_file))
        print(f"OK - Arquivo compilado: {mo_file}")
    except Exception as e:
        print(f"Erro ao compilar {po_file}: {e}")
        sys.exit(1)
else:
    print(f"Erro: Arquivo nao encontrado: {po_file}")
    sys.exit(1)

print("Traducoes compiladas com sucesso!")
