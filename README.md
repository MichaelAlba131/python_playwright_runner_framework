<!DOCTYPE html>
<html lang="pt-BR">
<body>
<section>
  <h1><span class="emoji">🐍</span>Framework de Automação Playwright & Behave (Python)</h1>
  <p>Framework robusto para automação de testes de interface web utilizando <strong>Playwright</strong> e <strong>Pytest</strong> com geração de relatórios HTML completos.</p>
</section>

<section>
  <h2><span class="emoji">🚀</span>Setup Inicial</h2>
  <p>Configure seu ambiente para começar a rodar os testes facilmente:</p>
  <ol>
    <li>
      <strong>Crie e ative o ambiente virtual:</strong>
      <pre><code>python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows</code></pre>
    </li>
    <li>
      <strong>Instale as dependências e os navegadores do Playwright:</strong>
      <pre><code>pip install -r requirements.txt
python -m playwright install</code></pre>
    </li>
    <li>
      <strong>Execute os testes com relatório e paralelismo:</strong>
      <pre><code>pytest tests/ --html=report.html --self-contained-html</code></pre>
    </li>
    <li>
      <strong>Abra o relatório gerado:</strong>
      <code>report.html</code>
    </li>
  </ol>
</section>

<section>
<h2>🏗️ Estrutura do Projeto</h2>
<pre><code>.
├── features/
│   ├── environment.py              # Hooks (setup e teardown dos testes)
│   ├── interactions/
│   │   └── login_interactions.py   # Ações encapsuladas (ex: login)
│   ├── steps/
│   │   └── login_steps.py          # Steps BDD para o login
│   └── login.feature               # Feature file (cenários BDD)
├── pages/
│   └── login_page.py               # Page Object Model (elementos da página)
├── runners/
│   └── parallel_runner.py          # Script para execução paralela dos testes
├── utils/
│   └── utils.py                    # Utilitários (espera dinâmica, etc)
├── requirements.txt                # Dependências do projeto
└── README.md                       # Esta documentação
</code></pre>
</section>

<section>
  <h2><span class="emoji">⚙️</span>Configurações e Execução</h2>
  <h3>Rodar todos os testes</h3>
  <pre><code>pytest tests/ --html=report.html --self-contained-html</code></pre>

<h3>Rodar teste específico</h3>
  <pre><code>pytest tests/test_login.py::test_successful_login --html=report.html --self-contained-html</code></pre>

<h3>Gerar relatório HTML customizado com screenshots</h3>
  <p>O framework captura prints automaticamente ao falhar, e adiciona no relatório HTML para facilitar a análise.</p>

<h3>Execução paralela com Playwright</h3>
  <p>Você pode configurar paralelismo editando o arquivo <code>pytest.ini</code> ou usar a CLI do Playwright para múltiplos browsers:</p>
  <pre><code>playwright test --workers=4</code></pre>
  <p>Ou no <code>pytest.ini</code>:</p>
  <pre><code>[pytest]
addopts = -n 4</code></pre>
</section>

<section>
  <h2><span class="emoji">🛠️</span>Dicas e Troubleshooting</h2>
  <ul>
    <li>⚠️ <strong>ModuleNotFoundError: playwright</strong> — certifique-se que o ambiente virtual está ativado e que o Playwright está instalado.</li>
    <li>🚫 <strong>pytest não reconhece opções --html</strong> — verifique se o plugin <code>pytest-html</code> está instalado.</li>
    <li>📂 Erro <code>No steps directory</code> no Behave — garanta que a estrutura de pastas está correta e que há arquivos de steps.</li>
    <li>🧹 Sempre feche browsers no final dos testes para evitar vazamento de recursos.</li>
    <li>📅 Atualize dependências regularmente para evitar incompatibilidades.</li>
  </ul>
</section>

<section>
  <h2><span class="emoji">📦</span>Arquivo requirements.txt</h2>
  <pre><code>playwright==1.32.0
pytest==8.4.0
pytest-playwright==0.7.0
pytest-html==4.1.1</code></pre>
</section>

<h2>🤝 Contribuição</h2>
<p>Contribuições são bem-vindas! Abra uma issue ou faça um pull request para melhorias, correções e novas features.</p>

<hr/>

<h2>🪪 Licença</h2>
<p>
Distribuído sob a licença MIT. Veja o arquivo <code>LICENSE</code> para mais informações.
</p>
</body>
</html>
