import click
import numpy as np
from numpy import pi
import pandas as pd


@click.group()
def cmd_group():
    pass


@cmd_group.command()
@click.option(
    "--number",
    "-n",
    help = "Chooses the amount of numbers in between x = 0 and 2pi",
    default = 10,
    show_default = True,
)
def sin(number):
    """Makes a sine function from a lineair list (np.linspace) of x-values from 0 to 2pi.
        
        Args: number (int) amount of numbers in between x = 0 and 2pi """
    
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return

@cmd_group.command()
@click.option(
    "--number",
    "-n",
    help = "Chooses the amount of numbers in between x = 0 and 2pi",
    default = 10,
    show_default = True,
)
def tan(number):
    """ Makes a tan function from a lineair list (np.linspace) of x-values from 0 to 2pi.
        
        Args: number (int) amount of numbers in between x = 0 and 2pi"""
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return

if __name__ == "__main__":
    cmd_group()