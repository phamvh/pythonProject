import pandas as pd
"""
https://www.w3schools.com/python/pandas/pandas_intro.asp
"""

if __name__ == '__main__':
    # Some simple dataset mimicking a table
    mydataset = {
        'cars': ["BMW", "Volvo", "Ford"],
        'passings': [3, 7, 2]
    }
    table = pd.DataFrame(mydataset)
    print(table)
    # this prints the following table
    """
        cars  passings
    0    BMW         3
    1  Volvo         7
    2   Ford         2
    """
    print(pd.__version__)

    """
    A pandas series is like a column in a table.
    It is a one-d array holding data of any type.
    """
    a = [1,2,3]
    series = pd.Series(a)
    print(a) # [1, 2, 3]

    """
    Labels are used to access data of a column.
    If no labels are specified, data can be accessed using index starting from 0.
    So, in short:
      - without labels, a series is just a python list. Use index to access elements
      - with labels, a series is a like a dict: use labels to access elements
    """
    print(series[0]) # 1
    # now we can give each column a label (name) using keyword arg "index"
    series = pd.Series(a, index=['x', 'y', 'z'])
    print(series)
    # the above statement gives the following output
    """
    x    1
    y    2
    z    3
    """
    # now we can access each value using its label
    print(series['y']) # 2

    """
    We can use key-value object as Series like a dict, so keys in the dict are used as labels.
    """
    calories = {'day1': 1000, 'day2': 1500, 'day3': 2000}
    series = pd.Series(calories)
    print(series)
    """
    days1    1000
    days2    1500
    days3    2000
    """
    print(series['day2']) # 1500
    # You can select just some of the keys in the dict to build a series, and not all of them.
    # the series will include only those keys and their values
    series = pd.Series(calories, index=['day1', 'day2'])
    print(series)
    # output
    """
    day1    1000
    day2    1500
    """
    ######## Operations with a series: there are tons of them
    print(series.max()) # 1500
    print(series.min()) # 100
    print(series.head(1)) # day1    1000
    print(series.head(2)) # print both rows: for day1 and day2
    print(series.count()) # 2



    print()
    print("DataFrame")
    """
    DataFrame: is a just multi-D table.
    Series is just a column of a table, while a DatFrame is a whole table
    """
    data = {
      "products": ['carrot', 'potato', 'celery'],
      "prices": [2, 3, 4]
    }

    # this creates a table-like data, where:
    #  products[0] and prices[0] forms the first row
    #  products[1] and prices[1] forms the first row, etc
    df = pd.DataFrame(data)
    print(df)
    # output
    """ first column is just the index of each row, second column is product, and third column is price
      products  prices
    0   carrot       2
    1   potato       3
    2   celery       4
    """
    # use loc to get a specific row.
    print(df.loc[0])
    """ return the first row
    products    carrot
    prices           2
    """
    # if you don't want those default numeric index (0, 1, 2), you can give each row a label
    df = pd.DataFrame(data, index=["veggie1", "veggie2", "veggie3"])
    print(df)
    """
            products  prices
    veggie1   carrot       2
    veggie2   potato       3
    veggie3   celery       4
    """
    # now, to use lock, provide the row name (label) instead of index
    print(df.loc["veggie1"])
    print()
    # Operations with DataFrame
    print(df.keys()) # Index(['products', 'prices'], dtype='object')
    print(df.head(1))
    print(df.tail(1))
    print()
    print(df.info())


    ###### CLEANING DATA
    print("===================")
    data = {
        "products": ['carrot', 'potato', 'celery', 'chicken'],
        "prices": [2, 3, 4, None]
    }
    df = pd.DataFrame(data)
    print(df.count()) # products    4   prices      3
    df = df.dropna() # drop rows with empty cells
    print(df.count()) # products    3   prices      3
    df.plot()
    import matplotlib.pyplot as plt
    plt.show() # this opens up a window showing a graph.


