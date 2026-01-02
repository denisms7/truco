# Como Adicionar Google AdSense ao Placar de Truco

Este guia explica como integrar anúncios do Google AdSense ao seu placar de truco para monetização.

## 📍 Áreas de Anúncio Disponíveis

O placar possui **3 áreas estratégicas** para anúncios:

1. **Topo** - Logo após o header, antes do título
2. **Meio** - Entre os placares e o botão de reset
3. **Rodapé** - Após o botão de reset

## 🚀 Passo a Passo

### 1. Crie uma conta no Google AdSense

Se ainda não tem uma conta:
- Acesse: https://www.google.com/adsense
- Cadastre-se com seu site/domínio
- Aguarde aprovação do Google (pode levar alguns dias)

### 2. Crie suas unidades de anúncio

No painel do AdSense:
1. Acesse **Anúncios** → **Por unidade de anúncio**
2. Clique em **Nova unidade de anúncio**
3. Escolha o tipo de anúncio

#### Tamanhos Recomendados:

**Para Topo e Rodapé:**
- Desktop: Banner 728x90
- Mobile: Banner 320x50 ou 320x100
- **Recomendação**: Use "Display responsivo" para adaptar automaticamente

**Para Meio:**
- Banner 728x90 (horizontal)
- Retângulo médio 300x250
- **Recomendação**: Retângulo médio 300x250 (melhor CTR)

### 3. Copie o código do anúncio

Após criar a unidade, o Google AdSense fornecerá um código similar a:

```html
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXXXXXXXX"
     crossorigin="anonymous"></script>
<!-- Nome da Unidade -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-XXXXXXXXXXXXXXXX"
     data-ad-slot="XXXXXXXXXX"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
```

### 4. Cole o código no arquivo HTML

Abra o arquivo: `score/templates/score/index.html`

Encontre os comentários indicando onde colar:

**Exemplo - Anúncio do Topo (linha ~29-32):**
```html
<div class="ad-content">
    <!-- Cole aqui seu código do Google AdSense -->
    <!-- COLE O CÓDIGO AQUI -->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXXXXXXXX"
         crossorigin="anonymous"></script>
    <ins class="adsbygoogle"
         style="display:block"
         data-ad-client="ca-pub-XXXXXXXXXXXXXXXX"
         data-ad-slot="XXXXXXXXXX"
         data-ad-format="auto"
         data-full-width-responsive="true"></ins>
    <script>
         (adsbygoogle = window.adsbygoogle || []).push({});
    </script>
</div>
```

Repita para as outras 2 áreas (meio e rodapé).

### 5. Adicione o código de verificação (primeira vez)

Na primeira configuração, o Google pedirá para adicionar um código no `<head>`:

No arquivo `score/templates/score/index.html`, adicione entre as tags `<head>`:

```html
<head>
    <!-- ... outros códigos ... -->

    <!-- Google AdSense Verificação -->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXXXXXXXX"
         crossorigin="anonymous"></script>

    <!-- ... -->
</head>
```

## 💡 Dicas para Maximizar Ganhos

1. **Use anúncios responsivos** - Se adaptam automaticamente ao tamanho da tela
2. **Teste diferentes posições** - Monitore qual área tem melhor CTR
3. **Não exagere** - 3 anúncios por página é um bom equilíbrio
4. **Aguarde alguns dias** - Os anúncios podem demorar para aparecer inicialmente
5. **Analise no Google Analytics** - Acompanhe visualizações de página e cliques

## 🎨 Design das Áreas de Anúncio

As áreas foram estilizadas para combinar com o design do placar:
- Background com glassmorphism (vidro fosco)
- Borda sutil
- Label "Publicidade" discreta
- Totalmente responsivo

## ⚠️ Avisos Importantes

1. **Não clique nos próprios anúncios** - Isso pode banir sua conta
2. **Respeite as políticas do AdSense** - Leia os termos de serviço
3. **Conteúdo adequado** - Certifique-se que seu site segue as diretrizes
4. **Tráfego legítimo** - Não use bots ou tráfego falso

## 📊 Acompanhamento

Após configurar, monitore seus ganhos em:
- https://www.google.com/adsense

Métricas importantes:
- **RPM** (Revenue per Mille) - Ganho por 1000 visualizações
- **CTR** (Click Through Rate) - Taxa de cliques
- **CPC** (Cost Per Click) - Valor por clique

## 🆘 Problemas Comuns

**Anúncios em branco:**
- Aguarde 24-48 horas após adicionar o código
- Verifique se o código foi colado corretamente
- Confirme se sua conta foi aprovada

**Anúncios não aparecem:**
- Limpe o cache do navegador
- Teste em modo anônimo/privado
- Verifique o console do navegador (F12) para erros

**Conta suspensa:**
- Entre em contato com o suporte do Google AdSense
- Revise as políticas que pode ter violado

## 📞 Suporte

- Google AdSense Help: https://support.google.com/adsense
- Fórum AdSense: https://support.google.com/adsense/community

---

Boa sorte com sua monetização! 🚀💰
