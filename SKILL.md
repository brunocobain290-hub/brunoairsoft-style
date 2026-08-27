---
name: brunoairsoft-style
description: "Diretrizes visuais, editoriais e operacionais para criar conteúdo do perfil @brunoairsoft_, incluindo geração de imagens táticas com fidelidade às referências do Bruno, sincronização de fotos do Google Drive, aplicação da identidade visual e produção de legendas otimizadas para Instagram."
---

# Bruno Airsoft Style

Use esta habilidade para criar imagens, posts, Stories, Reels, legendas e chamadas de engajamento para o perfil **@brunoairsoft_**. Preserve consistência visual, fidelidade às referências oficiais e o tom motivacional do perfil.

## Identidade visual

Aplique a estética **Dark Tactical / Profissional de Elite**, com preto, tan/coyote e verde oliva como cores predominantes. Use vermelho nas lentes e pontas de segurança da AEG; use laranja/âmbar ou ciano/neon somente quando o conceito pedir impacto ou tecnologia.

Use iluminação dramática, alto contraste, sombras marcadas e luzes direcionais com aparência cinematográfica. Para títulos de impacto, use **League Gothic**, preferencialmente em caixa alta (ALL CAPS). Mantenha composição profissional, legível e adequada para redes sociais.

## Referências oficiais do Bruno

Priorize a fidelidade visual às fotos oficiais. Utilize as imagens em `templates/` como referências-base:

1. `templates/referencia_principal.webp`: iluminação, pose tática e qualidade geral.
2. `templates/referencia_rosto.jpg`: traços faciais e expressão.
3. `templates/referencia_perfil.webp`: acessórios, boné tan e óculos vermelhos.
4. `templates/drive_references/`: fotos oficiais sincronizadas do Google Drive, usadas para selecionar rosto, equipamento, camuflagem, acessórios e aparência mais recente.

### Sincronização do Google Drive

Antes de gerar imagens quando houver possibilidade de atualização das referências, sincronize a pasta oficial do Drive executando:

```bash
python3 /home/ubuntu/skills/brunoairsoft-style/scripts/sync_drive_images.py
```

O script usa a pasta do Drive configurada internamente e salva os arquivos em `templates/drive_references/`. Se a sincronização falhar por ausência de autenticação ou do comando `gws`, informe a limitação e utilize somente as referências locais já disponíveis; não invente novas características do Bruno.

## Regra de fidelidade total

Ao criar uma imagem, preserve **100% de consistência** com a referência escolhida:

1. Mantenha rosto, porte físico, cabelo, expressão e características faciais do Bruno.
2. Preserve o equipamento, colete, luvas, óculos vermelhos, boné, shemagh e demais acessórios observados na referência.
3. Reproduza exatamente a camuflagem da referência. Os padrões aceitos são **MARPAT (Digital Woodland), MULTICAM, TAN/COYOTE e MULTICAM BLACK**.
4. Mantenha o uniforme limpo, sem emblemas, patches ou faixas coloridas nos braços, salvo quando o usuário solicitar explicitamente.
5. Quando houver uma AEG, inclua uma pequena ponta vermelha ou laranja, aproximadamente 1 cm, na extremidade do cano, conforme a identidade visual de segurança do perfil.
6. Altere principalmente a **pose** e a **ambientação**. Não altere arbitrariamente rosto, equipamento, camuflagem ou acessórios.

## Padrão de prompt para geração de imagens

Ao gerar uma imagem, adapte este padrão ao briefing do usuário:

- **Sujeito:** “Exactly the man from the selected reference photo, maintaining 100% facial, physical and gear consistency.”
- **Equipamento:** “Identical tactical gear and accessories as the reference, holding a professional AEG rifle with an approximately 1cm red or orange safety tip.”
- **Camuflagem:** “Use the exact camouflage pattern from the reference photo: MARPAT, MULTICAM, TAN/COYOTE, or MULTICAM BLACK.”
- **Cenário:** “Cinematic action environment, tactical forest, dark workshop, battlefield, or high-tech neon setting, according to the brief.”
- **Atmosfera:** “Cinematic lighting, moody, professional photography, action-movie aesthetic, high contrast.”
- **Texto:** “Bold H1 text overlay in League Gothic style, preferably white or with a warm orange/amber glow; keep text short, legible and correctly spelled.”

Revise a imagem final para verificar identidade, equipamento, camuflagem, segurança da AEG, legibilidade e proporção antes de entregá-la.

## Formatos

- **Feed:** proporção 3:4, preferencialmente 1792 × 2400 px.
- **Stories e Reels:** proporção 9:16.
- Respeite áreas seguras para textos e elementos importantes em Stories e Reels.

## Diretrizes de legendas para Instagram

Escreva legendas com tom **motivacional, incentivador e autêntico**, focado em superação, disciplina, camaradagem e evolução no airsoft. Otimize o texto para alcance e descoberta, usando naturalmente termos como “Airsoft”, “esporte tático”, “equipamento tático”, “treino”, “disciplina” e “camaradagem” quando forem pertinentes.

### Estrutura obrigatória

1. **GANCHO — primeira frase**
   - Escreva em **CAIXA ALTA**.
   - Torne-o impactante e orientado à ação.
   - Comece sempre com um emoji relevante.
   - Exemplo: `🚨 SALVE ESSE POST PRA ELE TE SALVAR DEPOIS.`

2. **DESCRIÇÃO OTIMIZADA — desenvolvimento**
   - Explique o conteúdo de maneira natural e completa.
   - Use palavras-chave relevantes para Instagram e Google sem forçar repetições.
   - Limite cada parágrafo a no máximo **3 linhas**.
   - Comece cada parágrafo com um emoji relacionado ao conteúdo.
   - Conecte o assunto a treino, estratégia, equipamento, segurança, disciplina ou evolução quando fizer sentido.

3. **PALAVRAS-CHAVE ESTRATÉGICAS — encerramento**
   - Insira de **7 a 15 palavras-chave ou termos** relacionados ao conteúdo.
   - Não use o símbolo `#`; escreva somente as palavras ou expressões.

### Elementos obrigatórios junto com cada legenda

Entregue sempre os dois itens abaixo, além da legenda principal:

1. **📌 Comentário para fixar:** escreva um comentário curto e instigante para gerar a primeira onda de engajamento ou reforçar o CTA principal.
2. **📲 CTA para grupos do WhatsApp:** siga o padrão de convocação de guerreiro. Comece com `Salve guerreiros(a), [post novo/reels novo] no ar! ⚔️🔥`, desenvolva uma breve reflexão ou gancho sobre o conteúdo e finalize pedindo uma curtida e um comentário para “fortalecer”. Exemplo de encerramento: `Quem puder fortalecer com uma curtida e comentário, agradeço demais! 👊👇`

## Formato recomendado de entrega

Quando o usuário pedir uma legenda, entregue nesta ordem: **Legenda**, **Comentário para fixar**, **CTA para grupos do WhatsApp** e **Palavras-chave**. Quando pedir uma imagem ou post, confirme mentalmente a referência utilizada, o formato, a camuflagem, a fidelidade do equipamento e a legibilidade dos textos antes de finalizar.

## Ativos e documentos

A logo oficial está em `assets/logo_skill.png`. Os termos de propriedade intelectual, restrições de uso e isenção de responsabilidade estão em `docs/TERMOS_LEGAIS.md`; consulte esse documento antes de orientar uso comercial da skill. O manual complementar está em `docs/MANUAL_USUARIO.md`.
