---
name: brunoairsoft-style
description: "Criação de posts, imagens, Stories, Reels, legendas e chamadas para o perfil @brunoairsoft_, com geração de novas imagens do Bruno, fidelidade rigorosa às referências oficiais e aplicação do padrão tipográfico Dark Tactical do perfil."
---

# Bruno Airsoft Style

Use esta skill para criar imagens, posts, Stories, Reels, legendas e chamadas de engajamento para o perfil **@brunoairsoft_**. Preserve a identidade visual, a autenticidade do Bruno Airsoft e o tom motivacional, disciplinado e respeitoso do esporte.

## Regra principal de geração

Gere sempre uma **imagem nova do Bruno Airsoft** de acordo com o conteúdo do post. Não reutilize literalmente uma fotografia anterior nem faça apenas uma troca de texto sobre uma foto já usada. Use as referências oficiais para manter identidade, rosto, porte, acessórios, shemagh e camuflagem, mas crie nova pose, novo enquadramento, nova iluminação ou nova ambientação.

Quando o usuário fornecer uma imagem de design, trate-a somente como referência de **tipografia, composição, textura, cores e hierarquia textual**, salvo instrução explícita em contrário. Não copie as pessoas, fotografias ou elementos visuais da imagem de design.

## Fidelidade obrigatória ao Bruno

Nunca gere o Bruno usando boné, gorro, capacete ou outra cobertura semelhante. Utilize somente **shemagh full**, cobrindo completamente cabeça, pescoço e rosto, combinado com os óculos de proteção vermelhos observados nas referências.

Reproduza somente os padrões de camuflagem efetivamente presentes nas referências oficiais selecionadas para o trabalho. Não invente, combine, estilize ou substitua camuflagens. Não use um padrão genérico apenas porque parece militar. Se a referência escolhida mostrar MARPAT/digital woodland, reproduza esse padrão; se mostrar outro padrão oficial, reproduza exatamente o padrão daquela referência.

Preserve colete, luvas, acessórios, proporções, postura corporal e configuração visual coerentes com a referência selecionada. Não invente patches, faixas, emblemas, cores de uniforme ou equipamentos que não estejam nas referências, salvo solicitação explícita do usuário. Quando uma AEG aparecer, inclua uma pequena ponta de segurança vermelha ou laranja, aproximadamente 1 cm, na extremidade do cano.

Antes de finalizar, verifique obrigatoriamente: ausência de boné; presença de shemagh full; camuflagem idêntica à referência selecionada; óculos vermelhos; acessórios coerentes; nova pose e nova fotografia; identidade visual plausível do Bruno; e ausência de elementos inventados.

## Referências oficiais

Priorize as referências locais disponíveis em `templates/` e `templates/drive_references/`. Use as referências de identidade para aparência, equipamento e camuflagem; não as trate como fotografias a serem copiadas.

As imagens de design fornecidas pelo usuário, incluindo posts com tipografia condensada e textura desgastada, devem ser usadas apenas para orientar o tratamento gráfico do texto. Se a sincronização do Google Drive estiver disponível, execute antes da geração:

```bash
python3 /home/ubuntu/skills/brunoairsoft-style/scripts/sync_drive_images.py
```

Se a sincronização falhar por falta de autenticação ou indisponibilidade do `gws`, informe a limitação e use somente as referências locais. Nunca invente características do Bruno para compensar a ausência de novas referências.

## Padrão obrigatório de design textual

Aplique o seguinte padrão quando o usuário indicar o estilo editorial dos posts anexados:

- Use fonte **alta, estreita, pesada e extremamente condensada**, em caixa alta, semelhante a League Gothic/Anton Condensed ou equivalente visual. Priorize a aparência vertical e militar da tipografia, sem fontes arredondadas, manuscritas ou modernas demais.
- Use fundo preto ou quase preto, com áreas amplas de negativo e tratamento Dark Tactical de alto contraste.
- Use branco envelhecido ou off-white para o texto principal. Aplique textura grunge/desgastada sutil, com pequenas irregularidades e marcas de uso, sem comprometer a leitura.
- Use laranja/âmbar queimado para palavras de abertura, conectores, datas, chamadas secundárias ou trechos de destaque. Não usar laranja neon.
- Organize o texto em blocos grandes, empilhados e centralizados ou alinhados à esquerda, conforme a composição. Dê maior escala às palavras-chave e mantenha margens seguras.
- Use linhas horizontais finas brancas para separar blocos quando isso reforçar a hierarquia.
- Preserve acentos, pontuação e grafia exatamente como fornecidos pelo usuário. Não permitir texto cortado, caracteres estranhos, palavras inventadas ou erros de português.
- Posicione a nova imagem do Bruno nas laterais, no fundo ou em uma área secundária, garantindo contraste suficiente para o texto. A pessoa não deve competir com a mensagem.
- Para feed, use proporção **3:4**, preferencialmente 1632 × 2176 px ou 1792 × 2400 px. Para Stories e Reels, use 9:16 e respeite áreas seguras.

### Prompt gráfico de referência

Ao adaptar o design textual, descreva a referência como: “tipografia militar muito condensada e alta, caixa alta, textura grunge desgastada, branco envelhecido e laranja/âmbar queimado, fundo preto, hierarquia editorial em blocos grandes, linha horizontal fina branca, margens seguras e alto contraste”. Use essa descrição apenas para o design; a fotografia deve ser nova e do Bruno conforme as regras de fidelidade.

## Diretrizes editoriais

Escreva mensagens motivacionais, autênticas e diretas sobre Airsoft, disciplina, respeito, honra, camaradagem, humildade, lealdade, evolução, fair play, liderança e espírito esportivo. Evite reduzir o conteúdo a equipamento, estética militar ou quantidade de disparos quando o objetivo for falar sobre caráter e valores.

Para legendas, comece com um gancho em caixa alta e emoji relevante. Desenvolva o assunto em parágrafos curtos, conectando-o ao treino, disciplina, segurança, respeito, camaradagem ou evolução. Ao final, inclua de 7 a 15 palavras-chave relacionadas, sem o símbolo `#`.

Quando uma legenda for solicitada, entregue na ordem: **Legenda**, **Comentário para fixar**, **CTA para grupos do WhatsApp** e **Palavras-chave**. O CTA deve começar com `Salve guerreiros(a), post novo no ar! ⚔️🔥` ou `Salve guerreiros(a), reels novo no ar! ⚔️🔥`, desenvolver uma breve reflexão e terminar pedindo curtida e comentário para fortalecer.

## Checklist final

Confirme que a arte usa uma fotografia nova do Bruno, sem boné e com shemagh full; que o padrão de camuflagem corresponde exatamente a uma referência oficial; que acessórios e proporções permanecem coerentes; que o design textual usa tipografia condensada, textura desgastada, preto, branco envelhecido e laranja/âmbar; que a frase está completa e legível; e que nenhum logotipo, marca d’água ou elemento inventado foi incluído sem autorização.

## Ativos

A logo oficial está em `assets/logo_skill.png`. Os termos legais estão em `docs/TERMOS_LEGAIS.md` e o manual complementar está em `docs/MANUAL_USUARIO.md`. Consulte esses arquivos quando a solicitação envolver uso comercial, direitos de imagem ou aplicação da marca.
