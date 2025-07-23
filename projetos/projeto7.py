for x in range(2):
    print("This is the outer loop iteration number" + str(x))
    for y in range(3 + 1):
        print("Inner loop iteration number " + str(x))
    print("Exit inner loop")