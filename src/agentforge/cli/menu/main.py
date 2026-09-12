import questionary

from agentforge.cli.common.console import console


def run_main_menu() -> None:
    while True:
        option = questionary.select(
            "¿What would you like to do?",
            choices=[
                "Create a new agent",
                "List existing agents",
                "List existing skills",
                "Exit"
            ],
        ).ask()

        if option == "Create a new agent":
            console.print("[green]Create a new agent[/green]")

        elif option == "List existing agents":
            console.print("[cyan]List existing agents[/cyan]")

        elif option == "List existing skills":
            console.print("[cyan]List existing skills[/cyan]")

        elif option == "Exit":
            break

        elif option is None:
            break