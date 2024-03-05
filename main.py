from cleaner import clean_folder
import typer

app = typer.Typer()

#TODO: addnt'l cmds here

@app.command()
def remove_files():
    pass

@app.command()
def clean_dir(dir_path: str):
    clean_folder(dir_path)


if __name__ == "__main__":
    app()