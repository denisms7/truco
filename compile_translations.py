#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para compilar mensagens de tradução usando polib
"""
import polib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
locale_dir = BASE_DIR / 'locale'

# Compila arquivo espanhol
po_file = locale_dir / 'es' / 'LC_MESSAGES' / 'django.po'
mo_file = locale_dir / 'es' / 'LC_MESSAGES' / 'django.mo'

if po_file.exists():
    print(f"Compilando: {po_file}")
    po = polib.pofile(str(po_file))
    po.save_as_mofile(str(mo_file))
    print(f"Arquivo compilado com sucesso: {mo_file}")
else:
    print(f"Arquivo nao encontrado: {po_file}")
