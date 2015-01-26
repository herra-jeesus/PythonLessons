"""
Ülesanne 14 - Sympy
Juhend: https://courses.cs.ttu.ee/w/images/3/32/ITI0140_2014_Loeng_matplotlib.pdf
"""
__author__ = "Borka Martin Orlov"
__email__ = "borka.orlov@gmail.com"

from matplotlib import pyplot
def get_data(file):
    """
    Read data from CSV file
    """
    data = {}
    data['years'] = []
    data['births'] = []
    data['deaths'] = []
    data['accretion'] = []

    for row in file:
        splitRow = row.split(';')
        data['years'].append( int(splitRow[0][1:-1]) )
        data['births'].append( int(splitRow[1]) )
        data['deaths'].append( int(splitRow[2]) )
        data['accretion'].append( int(splitRow[3]) )

    return data

def main():
    try:
        # Get data from CSV
        file = open("RV030sm.csv")
        data = get_data(file)

        # Plot the data
        fig, ax1 = pyplot.subplots()
        ax1.set_xlabel("Aasta")
        ax1.set_ylabel("Inimeste arv")

        ax1.plot(data['years'], data['births'], "g")
        ax1.plot(data['years'], data['deaths'], "r")
        ax2 = ax1.twinx()
        ax2.plot(data['years'], data['accretion'], "b")
        ax2.set_ylabel("accretion")
        pyplot.show()

    finally:
        file.close()

if __name__ == "__main__":
    main()
