import logging


def getValue(value):
    if(value < 0 or value > 100):
        raise ValueError("Value must be between 0 and 100")
    print("value=>", value)


def getGrade(value):
    try:
        getValue(value)
        print("grade value=>", value)
    except ValueError as e:
        print("exception=>", e)
    finally:
        print("finally")


getGrade(1000)

