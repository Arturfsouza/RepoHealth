import typer

app = typer.Typer(help="RepoHealth - análise de risco de manutenção em repositórios Git.")


@app.command()
def analyze(repo_url: str):
    typer.echo(f"Repositório informado: {repo_url}")


if __name__ == "__main__":
    app()