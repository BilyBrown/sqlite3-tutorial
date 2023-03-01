import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')


conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

# Showing how to create a table and name the columns(fields)
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

# Showsing how to insert data into columns
def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(14555552, '2016-01-01', 'Python', 8)")
    conn.commit()
    c.close()
    conn.close()

# Showing how to insert variables into the fields
def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0, 10)
    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
              (unix, date, keyword, value))
    conn.commit()

# Showing how to read from the db
def read_from_db():
    c.execute("SELECT * FROM stuffToPlot WHERE value=3 AND keyword='Python'")
    # data = c.fetchall() # the cursor has all of the selected data "selected/highlighted" fetchall or fetchone(one row) copies that data/those entries
    for row in c.fetchall():
        print(row[1])

# Showing how to graph data with matplotlib
def graph_data():
    c.execute("SELECT unix, value FROM stuffToPlot")
    data = c.fetchall()
    dates = []
    values = []
    for row in data:
        dates.append(datetime.datetime.fromtimestamp(row[0])) # Grabbing unix time and turning into datetime object, because we accidentally turned all of our datetime into strings when creating the database
        values.append(row[1])
    plt.plot_date(dates, values, '-')
    plt.show()

# Showing how to delete and update
def del_and_update():
    c.execute('SELECT * FROM stuffToPlot')
    [print(row) for row in c.fetchall()]

    # c.execute('UPDATE stuffToPlot SET value = 99 WHERE value = 6') # How to make the change
    # conn.commit()

    # c.execute('SELECT * FROM stuffToPlot')
    # [print(row for row in c.fetchall())]

    c.execute('DELETE FROM stuffToPlot WHERE value == 99') # BE VERY CAREFUL, THERE IS NO UNDO - Simple trick is to select what you want to delete, or print(len(of your selection))
    conn.commit()
    print(50* '#')

    c.execute('SELECT * FROM stuffToPlot')
    [print(row) for row in c.fetchall()]

        
# Creating/adding variable values to database
# create_table()
# data_entry()
# for i in range(50):
#     dynamic_data_entry()
#     time.sleep(1)
# read_from_db()
# graph_data()
del_and_update()


c.close()
conn.close()