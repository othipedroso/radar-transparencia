# 🏛️ Radar Transparência 2026

![Status](https://img.shields.io/badge/Status-Concluído-success)
![Tecnologia](https://img.shields.io/badge/Tech-HTML%20%7C%20CSS%20%7C%20JS-blue)
![Licença](https://img.shields.io/badge/License-MIT-yellow)

> **Fiscalização cidadã simplificada.** Uma ferramenta para monitorar gastos, votos e produtividade dos deputados federais brasileiros em tempo real, utilizando dados oficiais.

---

## 🔗 [Clique aqui para ver o Projeto Online](SEU_LINK_AQUI)

---

## 🎯 O Problema
Os dados do governo são públicos, mas muitas vezes **difíceis de entender** ou estão espalhados em diversas páginas burocráticas. O eleitor comum tem dificuldade em saber:
- Se o deputado gasta muito ou pouco em relação aos outros.
- Como ele votou em pautas importantes (Sim ou Não).
- Em quais áreas (Saúde, Segurança, Economia) ele realmente atua.

## 💡 A Solução: Radar Transparência
Este projeto consome a **API de Dados Abertos da Câmara dos Deputados** para criar um "Dossiê" instantâneo e visual de qualquer parlamentar.

### ✨ Principais Funcionalidades

1.  **💸 Termômetro de Gastos**
    - Calcula o total de gastos recentes.
    - Exibe uma **Barra Comparativa** visual: Gasto do Político vs. Teto da Cota (R$ 45k) vs. Média da Casa (R$ 31k).
    - Classifica automaticamente se o gasto está "Dentro do Padrão" ou "Acima da Média".

2.  **🗳️ Auditoria de Votos**
    - Busca os **votos nominais** (Sim/Não) registrados em plenário.
    - Em caso de falha da API ou votações simbólicas, gera automaticamente um link direto para o perfil oficial de auditoria na Câmara.

3.  **📊 Dashboard de Produtividade**
    - Analisa os Projetos de Lei (PLs) apresentados.
    - Agrupa automaticamente por temas: **Saúde, Segurança, Economia e Educação**.
    - Traduz o "juridiquês" das ementas para uma linguagem cidadã.

4.  **📱 Compartilhamento (Fator Viral)**
    - Botão integrado de **WhatsApp**.
    - Gera um resumo automático (Nome, Gasto e Link) para facilitar a disseminação da informação em grupos.

---

## 🛠️ Tecnologias Utilizadas

O projeto foi construído com **Vanilla JavaScript (JS Puro)**, sem dependência de frameworks pesados, garantindo leveza e facilidade de manutenção.

- **HTML5 Semantic**: Estrutura acessível.
- **CSS3 Moderno**: Variáveis (CSS Variables), Flexbox e Grid Layout.
- **JavaScript (ES6+)**: 
  - `fetch` API para consumo de dados assíncronos.
  - Manipulação de DOM para renderização dinâmica.
  - Tratamento de erros (Try/Catch) para blindar a aplicação contra instabilidades da API do governo.

## 🔌 API Consumida
Todos os dados são obtidos diretamente da fonte oficial, garantindo a idoneidade das informações:
- **Fonte:** [Dados Abertos - Câmara dos Deput
