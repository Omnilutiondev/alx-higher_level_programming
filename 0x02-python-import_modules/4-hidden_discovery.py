#!/usr/bin/python3
if __name__ == "__main__":
    """Print all hidden directories"""
    import hidden_4

    for px in dir(hidden_4):
        if px[:2] != "__":
            print(px)
