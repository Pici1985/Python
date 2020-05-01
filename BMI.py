olivabogyo = True if input("Kell oliva? i/n") == "i" else False
pepperoni = True if input("Kell pepperoni? i/n") == "i" else False
sonka = True if input("Kell sonka? i/n") == "i" else False

if (olivabogyo and pepperoni) and (pepperoni and not sonka):
    print("Fincsike...")


else:
    print("miaszar...")

print("a most ezt a szart itt atirtam elkuddom a gecibe!!!")
