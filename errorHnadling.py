try:
    a=10
except ZeroDivisionError as e:
    print("Error :",e)
except KeyError as e:
    print("KeyError")
except NameError as e:
    print("NameError")
except ValueError as e:
    print("ValueError",e)
finally:
    print("It is always run")