#!/usr/bin/env python
"""
Script para compilar mensagens de tradução sem precisar do gettext instalado.
Usa a biblioteca msgfmt do Python que vem com o Django.
"""
import os
import sys
from pathlib import Path

# Adiciona o projeto ao path
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

import django
django.setup()

from django.core.management import call_command

print("Compilando mensagens de tradução...")
try:
    # Tenta usar msgfmt do Python
    from django.core.management.commands.compilemessages import Command
    cmd = Command()
    cmd.handle(verbosity=2)
    print("✅ Traduções compiladas com sucesso!")
except Exception as e:
    print(f"❌ Erro ao compilar: {e}")
    print("\nTentando método alternativo...")

    # Método alternativo: usar polib
    try:
        import polib

        locale_dir = BASE_DIR / 'locale'
        po_file = locale_dir / 'es' / 'LC_MESSAGES' / 'django.po'
        mo_file = locale_dir / 'es' / 'LC_MESSAGES' / 'django.mo'

        if po_file.exists():
            po = polib.pofile(str(po_file))
            po.save_as_mofile(str(mo_file))
            print(f"✅ Arquivo compilado: {mo_file}")
        else:
            print(f"❌ Arquivo não encontrado: {po_file}")

    except ImportError:
        print("❌ polib não instalado. Instale com: pip install polib")
        print("\nVocê também pode instalar gettext:")
        print("  - Windows: https://mlocati.github.io/articles/gettext-iconv-windows.html")
        print("  - Ou use: pip install polib")
