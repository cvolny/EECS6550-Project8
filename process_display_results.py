import data_status as ds


def display_summary():
    print """Game Over

Results:
    Chances used: %d  Number Correct: %d

Thank you.
""" % (ds.chances_taken, len(ds.correctly_answered))

