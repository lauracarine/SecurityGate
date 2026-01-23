# SecurityGate

Projeto pessoal em Python com Docker, focado em **autenticação simples**, **requisição HTTP** e **construção de workflows de CI**, com ênfase em **verificações de segurança automatizadas** usando GitHub Actions.

---

## 💻 Funcionalidade

- Autenticação de usuário único  
- Redirecionamento após login bem-sucedido  
- Mensagem de erro em caso de credenciais inválidas  
- Estrutura mínima para testes de segurança em pipeline CI  
- Integração com ferramentas de análise estática e de dependências  

---

## 🔐 Credenciais de teste

> Apenas para fins educacionais e de demonstração.

- **Usuário:** `lauracarine`  
- **Senha:** `12345678`

---

## 🐳 Execução via Docker

1. Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/Projeto_user.git
```

2. Acesse a página do projeto:

```bash
cd Projeto_user
```

3. Construa a imagem Docker:
   
```bash
docker build -t projeto_user .
```

4. Execute o container:
   
```bash
docker run -p 8000:8000 projeto_user
```

5. Acesse no navegador:
 ```bash
[git clone https://github.com/SEU_USUARIO/Projeto_user.git](http://localhost:8000)
```
---
## 🔎 Pipeline de Segurança (CI)

O projeto utiliza **GitHub Actions** para executar verificações automáticas a cada `push` ou `pull request`, garantindo controle contínuo de qualidade e segurança do código.

### 🛠️ Ferramentas Utilizadas

- **Trivy**  
  Ferramenta de **SCA (Software Composition Analysis)**.  
  Responsável por identificar **CVEs (Common Vulnerabilities and Exposures)** em:
  - Imagens Docker  
  - Dependências do projeto  

- **Semgrep**  
  Ferramenta de **SAST (Static Application Security Testing)**.  
  Analisa o código-fonte Python em busca de:
  - Falhas de segurança  
  - Más práticas de desenvolvimento  
  - Vulnerabilidades mapeadas em **CWEs (Common Weakness Enumeration)**

### ✅ Objetivo do Pipeline

- Detectar vulnerabilidades **antes** do deploy  
- Impor uma **política de bloqueio** em caso de achados críticos  
- Padronizar boas práticas de segurança no ciclo de desenvolvimento  
- Servir como base de estudos em **DevSecOps**
## 📊 Resultados dos Scans

Os resultados das verificações de segurança ficam disponíveis diretamente no **GitHub Actions**.

### 🔍 Como acessar

1. Acesse o repositório no GitHub  
2. Clique na aba **Actions**  
3. Selecione o workflow de **Security Scan / CI**  
4. Abra a execução desejada para visualizar os logs

### 📌 O que é exibido

- **Trivy**
  - Vulnerabilidades encontradas na imagem Docker
  - Classificação por severidade (LOW, MEDIUM, HIGH, CRITICAL)

- **Semgrep**
  - Problemas de segurança no código-fonte
  - Indicação de regras violadas e arquivos afetados

### ✅ Status da execução

- **Sucesso (✔️)**: nenhuma vulnerabilidade crítica detectada  
- **Falha (❌)**: vulnerabilidades relevantes encontradas, acionando a política de bloqueio do pipeline

## ⚙️ Estrutura do Projeto

- `app/`  
  Código da aplicação (login e redirecionamento)

- `.github/workflows/`  
  Workflows do **GitHub Actions**  
  Responsáveis pela esteira de CI e pelos scans de segurança

- `Dockerfile`  
  Define a imagem da aplicação para análise e execução

- `requirements.txt`  
  Dependências do projeto (usado também nos scans SCA)

- `README.md`  
  Documentação do projeto, objetivos e fluxo da CI

  ## 📝 Observações

- Projeto desenvolvido com foco em **CI/CD e segurança**, não em regras de negócio complexas  
- O login existe apenas para **simular fluxo de autenticação** e permitir testes nos scans  
- Credenciais estão **hardcoded intencionalmente**, apenas para fins educacionais  
- Em cenários reais, senhas devem ser protegidas com:
  - Hash seguro
  - Variáveis de ambiente
  - Serviços de secret management
- Os scans executados no pipeline validam:
  - **SAST** → análise estática do código (Semgrep)
  - **SCA** → análise de dependências e CVEs (Trivy)
- A política de bloqueio garante que:
  - Builds com falhas de segurança **não avancem**
  - Pull Requests sejam barrados até correção
- Estrutura pensada para fácil reaproveitamento em outros projetos de estudo em DevSecOps



