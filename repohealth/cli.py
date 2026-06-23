import shutil

import typer

from repohealth.analyzer import analyze_repository
from repohealth.git_utils import clone_repository, create_temp_dir

app = typer.Typer(help="RepoHealth - análise de risco de manutenção em repositórios Git.")


@app.command()
def analyze(repo_url: str, limit: int = 10):
    temp_dir = create_temp_dir()

    try:
        typer.echo("Clonando repositório...")
        clone_repository(repo_url, temp_dir)

        typer.echo("Analisando histórico de commits...")
        result = analyze_repository(temp_dir)

        if not result:
            typer.echo("Nenhum arquivo foi encontrado para análise.")
            return

        typer.echo("\nRanking de arquivos com maior risco de manutenção:\n")

        for index, item in enumerate(result[:limit], start=1):
            typer.echo(f"{index}. {item['file']}")
            typer.echo(f"   Commits: {item['commits']}")
            typer.echo(f"   Autores: {item['authors']}")
            typer.echo(f"   Commits de correção: {item['bugfix_commits']}")
            typer.echo(f"   Score: {item['score']}")
            typer.echo(f"   Risco: {item['risk']}")
            typer.echo("")

    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)


if __name__ == "__main__":
    app()