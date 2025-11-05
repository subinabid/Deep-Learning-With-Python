import marimo

__generated_with = "0.17.7"
app = marimo.App(width="medium")


@app.cell
def _():
    a = 1
    print(a)
    return


@app.cell
def _():
    import marimo as mo
    mo.notebook_dir()
    return


if __name__ == "__main__":
    app.run()
