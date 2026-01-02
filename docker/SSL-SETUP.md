# Configuração SSL/TLS com Let's Encrypt

Este guia explica como configurar certificados SSL gratuitos para seu site.

## Pré-requisitos

1. Um domínio apontando para seu servidor (ex: `seusite.com`)
2. Portas 80 e 443 abertas e acessíveis na internet
3. Docker e docker-compose instalados

## Passo a passo

### 1. Configure seu domínio

Certifique-se que seu domínio (ex: `seusite.com`) está com DNS apontando para o IP do servidor.

### 2. Obtenha o certificado SSL

**Linux/Mac:**
```bash
chmod +x docker/scripts/init-letsencrypt.sh
./docker/scripts/init-letsencrypt.sh seusite.com seu-email@exemplo.com
```

**Windows (PowerShell):**
```powershell
docker-compose run --rm certbot certonly `
    --webroot `
    --webroot-path=/var/www/certbot `
    --email seu-email@exemplo.com `
    --agree-tos `
    --no-eff-email `
    -d seusite.com
```

### 3. Ative o SSL no Nginx

Edite `docker/nginx/default.conf` e:

1. **Descomente** o bloco de redirecionamento HTTP→HTTPS (linhas 11-15)
2. **Descomente** a linha `listen 443 ssl http2;` (linha 19)
3. **Descomente** o bloco de configuração SSL (linhas 22-29)
4. **Substitua** `your-domain` pelo seu domínio real
5. **Descomente** o header HSTS (linha 39)

Exemplo de alterações:
```nginx
# ANTES (comentado):
# listen 443 ssl http2;
# ssl_certificate /etc/letsencrypt/live/your-domain/fullchain.pem;

# DEPOIS (descomentado):
listen 443 ssl http2;
ssl_certificate /etc/letsencrypt/live/seusite.com/fullchain.pem;
ssl_certificate_key /etc/letsencrypt/live/seusite.com/privkey.pem;
```

### 4. Reinicie o Nginx

```bash
docker-compose restart nginx-proxy
```

### 5. Teste a configuração

Acesse seu site:
- `http://seusite.com` (deve redirecionar para HTTPS)
- `https://seusite.com` (deve funcionar com cadeado verde)

Teste a segurança em: https://www.ssllabs.com/ssltest/

## Renovação automática

Os certificados Let's Encrypt expiram em 90 dias, mas o container `certbot` renova automaticamente a cada 12 horas.

Para renovar manualmente:
```bash
docker-compose run --rm certbot renew
docker-compose restart nginx-proxy
```

## Recursos de segurança ativos

✅ **Rate Limiting**
- Máximo 10 requisições/segundo por IP
- Login limitado a 5 tentativas/minuto

✅ **Headers de Segurança**
- X-Frame-Options (proteção contra clickjacking)
- X-Content-Type-Options (proteção MIME sniffing)
- X-XSS-Protection (proteção XSS)
- Referrer-Policy (controle de referrer)
- Permissions-Policy (limita APIs do navegador)
- HSTS (quando SSL ativado)

✅ **Configuração SSL/TLS**
- TLS 1.2 e 1.3 apenas
- Ciphers seguros
- Session cache otimizado

## Troubleshooting

### Erro: "Connection refused"
- Verifique se as portas 80 e 443 estão abertas no firewall
- Teste: `telnet seu-ip 80`

### Erro: "DNS resolution failed"
- Verifique se o DNS está propagado: `nslookup seusite.com`
- Aguarde até 48h para propagação completa

### Erro: "Rate limit exceeded"
- Use o modo staging para testes (edite o script)
- Let's Encrypt tem limite de 5 certificados/semana por domínio
