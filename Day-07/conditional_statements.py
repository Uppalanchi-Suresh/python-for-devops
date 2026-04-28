instance_type = input("Enter the instance type (e.g., t2.micro, t2.small): ")

if instance_type == "t2.micro":
    print("t2.micro is a small instance type with 1 vCPU and 1 GB of RAM.")
elif instance_type == "t2.small":
    print("t2.small is a medium instance type with 1 vCPU and 2 GB of RAM.")
else:
    print("Unknown instance type.")