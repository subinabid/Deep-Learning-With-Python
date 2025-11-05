import marimo

__generated_with = "0.17.7"
app = marimo.App()


@app.cell
def _():
    import numpy as np
    x = np.array(12)
    x
    return (x,)


@app.cell
def _(x):
    x.ndim
    return


if __name__ == "__main__":
    app.run()

