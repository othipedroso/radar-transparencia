# 🏛️ Radar Transparência 2026

![GitHub deployments](https://img.shields.io/github/deployments/othipedroso/radar-transparencia/github-pages?label=Deploy&logo=github&style=flat-square)
![GitHub language count](https://img.shields.io/github/languages/count/othipedroso/radar-transparencia?style=flat-square)
![GitHub top language](https://img.shields.io/github/languages/top/othipedroso/radar-transparencia?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

> **Fiscalização cidadã simplificada.** Uma ferramenta open source para monitorar gastos, votos e produtividade dos deputados federais brasileiros em tempo real, traduzindo dados oficiais para uma linguagem acessível.

---

## 🔗 [Acesse o Projeto Online Aqui](https://othipedroso.github.io/radar-transparencia/)

---

## 🎯 O Propósito
Os dados do governo brasileiro são públicos, mas muitas vezes burocráticos, dispersos e difíceis de interpretar. O eleitor comum enfrenta barreiras para saber:
- Se o gasto de um deputado é abusivo ou está na média.
- Como ele votou em pautas polêmicas (Sim ou Não).
- Em quais áreas (Saúde, Segurança, Economia) ele realmente trabalha.

O **Radar Transparência** resolve isso consumindo a API oficial da Câmara e entregando um "Dossiê" visual e compartilhável.

---

## ✨ Funcionalidades Principais

### 1. 💸 Termômetro de Gastos Inteligente
Não mostramos apenas números soltos. O sistema cruza os dados para dar contexto:
- **Cálculo de Fluxo Recente:** Soma automática das últimas despesas.
- **Visualização Comparativa:** Uma barra de progresso compara o gasto do deputado com o **Teto da Cota (R$ 45k)** e a **Média da Casa (R$ 31k)**.
- **Status Dinâmico:** Alerta visual se o político está "Dentro do Padrão" ou "Acima da Média".

### 2. 🗳️ Auditoria de Votos Híbrida
Um sistema resiliente para garantir que a informação nunca falhe:
- Busca os **votos nominais** (Sim/Não) registrados em plenário.
- Identifica **votações simbólicas** (onde não há registro individual) e informa o usuário.
- Gera automaticamente links diretos para o **Perfil Oficial de Auditoria** na Câmara para verificação externa.

### 3. 📊 Dashboard de Produtividade
- Analisa centenas de Projetos de Lei (PLs) apresentados pelo parlamentar.
- **Categorização Automática:** Agrupa projetos por temas como Saúde, Segurança, Economia e Educação.
- **Tradutor de "Juridiquês":** Limpa os títulos das ementas (ex: remove "Dá nova redação ao art...") para facilitar a leitura.

### 4. 🚀 "Fator Zap" (Compartilhamento Viral)
- Botão integrado de **WhatsApp**.
- Gera um resumo automático com: **Nome + Partido + Gasto Total + Link Oficial**.
- Facilita a disseminação da informação em grupos de família e política.

---

## 🛠️ Tecnologias Utilizadas

O projeto foi construído com a filosofia **KISS (Keep It Simple, Stupid)**. Sem frameworks pesados, apenas a web pura para garantir performance máxima e facilidade de contribuição.

- **HTML5 Semântico**: Estrutura acessível e SEO-friendly.
- **CSS3 Moderno**: Uso de Variáveis (Custom Properties), Flexbox e Grid Layout para responsividade.
- **Vanilla JavaScript (ES6+)**: 
  - `fetch` API para consumo de dados assíncronos.
  - Manipulação de DOM reativa.
  - Tratamento de erros (`try/catch`) para blindar a aplicação contra instabilidades da API do governo.

---

## 🔌 API Consumida
Todos os dados são obtidos em tempo real diretamente da fonte oficial do Governo Federal:
- **Fonte:** [Dados Abertos - Câmara dos Deputados](https://dadosabertos.camara.leg.br/)
- **Endpoints:** `/deputados`, `/deputados/{id}/despesas`, `/deputados/{id}/votos`, `/proposicoes`.

---

## 🚀 Como rodar localmente

Se você quiser baixar o código para estudar ou modificar:

1. Clone este repositório:
   ```bash
   git clone [https://github.com/othipedroso/radar-transparencia.git](https://github.com/othipedroso/radar-transparencia.git)
