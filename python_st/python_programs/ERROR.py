try:
    a=int(input())
    b=int(input())
    print(a/b)

except ValueError as e:
    print(e)

except NameError as h:
    print(h)

except TypeError as k:
    print(k)
except Exception as r:
    print("somthinking went wrong:{}")
finally:
    print(a)