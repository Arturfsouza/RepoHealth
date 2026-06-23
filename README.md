## RepoHealth

### 1. Membros do Grupo

Artur Fonseca de Souza

### 2. Explicação do Sistema

O RepoHealth é uma ferramenta de linha de comando (CLI) desenvolvida para identificar problemas de manutenção em projetos de software por meio da mineração de repositórios Git e GitHub.

A ferramenta permite analisar repositórios remotos diretamente do GitHub, coletando dados do histórico de commits e do código-fonte para identificar arquivos com maior risco de manutenção.

Principais fatores analisados:

* Frequência de alterações em arquivos;
* Número de desenvolvedores que modificaram um arquivo;
* Complexidade do código;
* Tamanho dos arquivos em linhas de código;
* Presença de commits relacionados a correções de bugs, como `fix`, `bug` e `error`.

A partir dessas informações, o sistema gera um relatório no terminal destacando os arquivos com maior risco de manutenção. Esse ranking pode auxiliar desenvolvedores na identificação de partes do código que merecem maior atenção durante atividades de manutenção e evolução.

### 3. Tecnologias Utilizadas

O projeto foi desenvolvido utilizando as seguintes tecnologias:

#### Linguagem

* Python

#### Mineração de Repositórios

* PyDriller: análise de commits e histórico de alterações.
* GitPython: clonagem e manipulação de repositórios Git.

#### Interface de Linha de Comando

* Typer: criação da CLI.

#### Métricas de Código

* Lizard: cálculo de complexidade ciclomática.
* Contagem própria de linhas de código: usada para medir o tamanho dos arquivos analisados.

#### Testes e Integração Contínua

* Pytest: criação e execução dos testes unitários.
* GitHub Actions: execução automática dos testes a cada push ou pull request.

### 4. Como instalar a ferramenta

Clone o repositório:

```bash
git clone https://github.com/Arturfsouza/RepoHealth.git
```

Acesse a pasta do projeto:

```bash
cd RepoHealth
```

Crie um ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual.

No Linux ou WSL:

```bash
source venv/bin/activate
```

No Windows:

```bash
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

### 5. Como utilizar a ferramenta

Execute o comando abaixo informando a URL de um repositório GitHub:

```bash
python -m repohealth.cli https://github.com/usuario/repositorio
```

Exemplo:

```bash
python -m repohealth.cli https://github.com/pallets/flask --limit 5
```

A ferramenta exibirá no terminal um ranking dos arquivos com maior risco de manutenção, mostrando informações como:

* número de commits;
* número de autores;
* commits relacionados a correções;
* linhas de código;
* complexidade;
* score de risco;
* classificação do risco.

### 6. Como executar os testes localmente

Execute:

```bash
pytest
```

O projeto possui testes unitários para validar as principais funções da ferramenta, incluindo cálculo de score, classificação de risco, análise de commits, manipulação de repositórios e métricas de código.

### 7. GitHub Actions

Os testes são executados automaticamente pelo GitHub Actions a cada push ou pull request realizado no repositório.

### 8. Possíveis Extensões Futuras

* Integração com PyGithub;
* Uso da GitHub REST API;
* Análise de issues, pull requests e contribuidores;
* Geração de relatórios em HTML ou CSV;
* Visualização de métricas com gráficos;
* Exportação dos resultados para arquivos externos.
