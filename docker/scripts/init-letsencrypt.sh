#!/bin/bash

# Script para inicializar certificados SSL com Let's Encrypt
# Uso: ./init-letsencrypt.sh seu-dominio.com seu-email@exemplo.com

if [ "$#" -ne 2 ]; then
    echo "Uso: $0 <dominio> <email>"
    echo "Exemplo: $0 meusite.com admin@meusite.com"
    exit 1
fi

DOMAIN=$1
EMAIL=$2
STAGING=0  # Mude para 1 para testar (evita rate limiting)

echo "### Obtendo certificado SSL para $DOMAIN..."

if [ $STAGING != "0" ]; then
  STAGING_ARG="--staging"
fi

# Criar diretórios necessários
mkdir -p certbot/conf
mkdir -p certbot/www

# Obter certificado
docker-compose run --rm certbot certonly \
    --webroot \
    --webroot-path=/var/www/certbot \
    $STAGING_ARG \
    --email $EMAIL \
    --agree-tos \
    --no-eff-email \
    -d $DOMAIN

if [ $? -eq 0 ]; then
    echo ""
    echo "### Certificado obtido com sucesso!"
    echo "### Agora você precisa:"
    echo "1. Editar docker/nginx/default.conf"
    echo "2. Descomentar as linhas SSL (listen 443, ssl_certificate, etc)"
    echo "3. Substituir 'your-domain' por '$DOMAIN'"
    echo "4. Reiniciar nginx: docker-compose restart nginx-proxy"
else
    echo ""
    echo "### Erro ao obter certificado!"
    echo "### Verifique se:"
    echo "1. O domínio $DOMAIN está apontando para este servidor"
    echo "2. As portas 80 e 443 estão acessíveis"
fi
