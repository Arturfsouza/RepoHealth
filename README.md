## RepoHealth
### 1. Membros do Grupo
Artur Fonseca de Souza

### 2. Explicação do Sistema

O Repo Maintain Check é uma ferramenta de linha de comando (CLI) desenvolvida para identificar problemas de manutenção em projetos de software por meio da mineração de repositórios Git e GitHub.
A ferramenta permite analisar repositórios remotos diretamente do GitHub, coletando dados do histórico de commits e do código-fonte para identificar arquivos com maior risco de manutenção.

Principais fatores analisados:

Frequência de alterações em arquivos;
Número de desenvolvedores que modificaram um arquivo;
Complexidade do código;
Tamanho dos arquivos (linhas de código);
Presença de commits relacionados a correções de bugs (ex: “fix”, “bug”, “error”).

A partir dessas informações, o sistema gera relatórios que destacam arquivos e áreas do código com maior risco de manutenção.

### 3. Tecnologias Utilizadas

O projeto será desenvolvido utilizando as seguintes tecnologias:

Linguagem: Python

Mineração de Repositórios:
PyDriller: análise de commits e histórico de alterações
GitPython: clonagem e manipulação de repositórios

Integração com GitHub:
PyGithub: acesso a dados como issues, pull requests e contribuidores
GitHub REST API: coleta de dados adicionais do repositório

Interface de Linha de Comando:
Typer: criação da CLI

Métricas de Código:
Lizard: cálculo de complexidade ciclomática
cloc: contagem de linhas de código

Possíveis Extensões Futuras:

Geração de relatórios em HTML ou CSV
Visualização de métricas com gráficos
Sistema de pontuação de risco automatizado
