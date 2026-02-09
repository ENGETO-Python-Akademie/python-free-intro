for method in dir(str):
    if not method.startswith("_"):
        print(method)