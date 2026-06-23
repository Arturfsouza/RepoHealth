import typer

from repohealth.analyzer import analyze_repository
from repohealth.git_utils import clone_repository, create_temp_dir

app = typer.Typer(help="RepoHealth - análise de risco de manutenção em repositórios Git.")


@app.command()
def analyze(repo_url: str):
    temp_dir = create_temp_dir()

    typer.echo("Clonando repositório...")
    clone_repository(repo_url, temp_dir)

    typer.echo("Analisando histórico de commits...")
    result = analyze_repository(temp_dir)

    typer.echo(f"Arquivos analisados: {len(result)}")


if __name__ == "__main__":
    app()