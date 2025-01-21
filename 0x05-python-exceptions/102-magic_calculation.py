#!/usr/bin/python3
def magic_calculation(a, b):
    rst = 0
    for itm in range(1, 3):
        try:
            if itm > a:
                raise Exception("Too far")
            else:
                rst += a ** b / itm
        except Exception:
            rst = b + a
            break
    return (rst)
