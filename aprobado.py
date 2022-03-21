import sys

if len(sys.argv)==3:

    print(f"nota 1 es: {sys.argv[1]} \n\n")
    print(f"nota 2 es: {sys.argv[2]} \n\n")

    if ((int(sys.argv[1]) + int(sys.argv[2]) ) / 2 > 7):
        print ("muy bien, estas promocionado")

    else:
        print("no aprobo")

