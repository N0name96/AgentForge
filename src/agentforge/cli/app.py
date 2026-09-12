import typer
from rich.console import Console
from rich.panel import Panel

from agentforge.cli.menu.main import run_main_menu
from agentforge.cli.common.console import console


app = typer.Typer(
    invoke_without_command=True,
    no_args_is_help=False
)


@app.callback(invoke_without_command=True)
def root(ctx: typer.Context) -> None:

    if ctx.invoked_subcommand is not None:
        return 

    console.print(
        Panel.fit(
            "[bold cyan]AgentForge CLI[/bold cyan]\n\n"
            "Agent Creation Toolkit"
        )
    )

    run_main_menu()


def main() -> None:
    app()


if __name__ == "__main__":
    main()