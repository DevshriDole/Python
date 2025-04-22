def pack_unpack_tuple():
    name = input("Enter name:")
    age = int(input("\nEnter age:"))
    city = input("\nEnter city:")
    country = input("\nEnter country:")

    person_info = (name, age, (city, country))
    print("\nInformation of the person is: ", person_info)
    name, age, (city, country) = person_info
    print("\nName of the person is: ", name)
    print("\nAge of the person is: ", age)
    print("\nCity is: ", city)
    print("\nCountry is: ", country)

pack_unpack_tuple()