product={101:["Kit kat",50,6],102:["Perk",30,2],103:["Galaxy",40,3]}

id=int(input("Enter the product id to search"))

res=product.get(id)

if res:
    print(f"Name    {res[0]}")
    print(f"Price   {res[1]}")
    print(f"Qty     {res[2]}")
else:
    print("Unavailable")

    