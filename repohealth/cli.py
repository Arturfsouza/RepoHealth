import typer

from repohealth.git_utils import create_temp_dir

app = typer.Typer(help="RepoHealth - análise de risco de manutenção em repositórios Git.")


@app.command()
def analyze(repo_url: str):
    temp_dir = create_temp_dir()

    typer.echo(f"Repositório informado: {repo_url}")
    typer.echo(f"Pasta temporária criada: {temp_dir}")


if __name__ == "__main__":
    app()