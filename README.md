# 💸 Controle de Despesas Pessoais

Este projeto tem como objetivo oferecer uma **plataforma simples, intuitiva e visual** para **gerenciar finanças pessoais**, ajudando o usuário a **registrar, visualizar e analisar** suas movimentações financeiras de forma prática e eficiente.

---

## 🧠 Proposta

Muitas pessoas têm dificuldades em acompanhar seus gastos do dia a dia. Este sistema foi desenvolvido para resolver isso de maneira leve e interativa. Ele permite:

- Registrar entradas e saídas financeiras com categorização.
- Visualizar o histórico de transações.
- Acompanhar a **evolução mensal** dos gastos e rendimentos.
- Observar a **distribuição das despesas por categoria**.
- Anexar imagens de comprovantes, como notas fiscais ou recibos.

---

## 📋 Etapas de Desenvolvimento

### 1. 🧩 Entendimento do Problema
Antes de escrever qualquer linha de código, foi feita uma análise do cenário: **como as pessoas controlam suas finanças?**, **quais são as maiores dificuldades?**, **o que pode ser automatizado ou facilitado?**

### 2. 📝 Documentação Inicial
Antes de iniciar a codificação, documentamos todas as ideias: funcionalidades desejadas, estrutura de dados, fluxo de navegação e requisitos mínimos.

### 3. 🔧 Estruturação da Solução
Com a documentação em mãos, iniciamos a criação da arquitetura, dividida em camadas:
- Backend (API REST com Flask)
- Banco de dados (SQLite)
- Interface web (Streamlit)

### 4. 💡 Desenvolvimento Guiado por Conhecimento
A produção de código foi orientada por boas práticas adquiridas no **Curso de Python do Professor Rafael**, que forneceu uma base sólida para o projeto.

### 5. 🧪 Testes e Melhorias Contínuas
Fomos ajustando o sistema de acordo com as necessidades percebidas ao longo do desenvolvimento, aplicando melhorias e refinando a experiência do usuário.

---

## 🎥 Referência Visual

Veja um trecho de nós trabalhando nesse projeto:  
📽️ [Instagram Reel do projeto](https://www.instagram.com/reel/DKXRE34upcv/?utm_source=ig_web_copy_link&igsh=MWJzMTY2a3Zha3dqdA==)

---

## 🔎 Análise de Paradigmas e Boas Práticas

### Paradigmas Identificados

1. **Paradigma Imperativo**
   - Passo a passo claro das ações do programa.
   - Exemplo: criação de tabelas, inserção de dados, tratamento de requisições.

2. **Paradigma Procedural**
   - Estrutura baseada em funções reutilizáveis.
   - Exemplo: `adicionar_transacao()`, `obter_transacoes()`.

3. **Paradigma Declarativo**
   - Consultas SQL (`SELECT`, `GROUP BY`) expressam o que se deseja dos dados.
   - Plotly define gráficos de forma descritiva.

4. **Paradigma Reativo**
   - Com Streamlit, a interface responde automaticamente a alterações dos dados do usuário.

### Boas Práticas Adotadas

- ✅ **Modularização**
  - Separação clara: interface (Streamlit), lógica (Flask), persistência (SQLite).
  
- ✅ **API RESTful**
  - Uso de métodos HTTP corretos (GET, POST).
  - Retorno em JSON bem estruturado.

- ✅ **Segurança com SQL**
  - Placeholders (`?`) usados nas queries, prevenindo SQL Injection.

- ✅ **Visualização Clara**
  - Gráficos interativos com Plotly.
  - Dados tratados com pandas.

- ✅ **Responsividade**
  - Interface atualizada em tempo real com Streamlit.

- ✅ **Código Limpo**
  - Funções bem definidas, pequenas e reutilizáveis.
  - Organização por arquivos para facilitar a manutenção.

---

## ⚙️ Tecnologias Utilizadas

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: [Flask](https://flask.palletsprojects.com/)
- **Banco de Dados**: SQLite
- **Gráficos**: Plotly Express
- **Manipulação de Dados**: Pandas

---

## 🤝 Collaborators

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/GabrielMoreiradeSouza">
        <img src="https://avatars.githubusercontent.com/u/120267591?&v=4" width="100px;" alt="Foto do Iuri Silva no GitHub"/><br>
        <sub>
          <b>Gabriel Moreira</b>
        </sub>
      </a>
    </td>
        <td align="center">
      <a href="https://github.com/HugoParzival007">
        <img src="https://avatars.githubusercontent.com/u/90792051?v=4" width="100px;" alt="Foto do Iuri Silva no GitHub"/><br>
        <sub>
          <b>Hugo Guilherme</b>
        </sub>
      </a>
    </td>
        <td align="center">
      <a href="https://github.com/Djeyvid20">
        <img src="https://avatars.githubusercontent.com/u/142465826?v=4" width="100px;" alt="Foto do Iuri Silva no GitHub"/><br>
        <sub>
          <b>Deyvid Soares</b>
        </sub>
      </a>
    </td>
  </tr>
