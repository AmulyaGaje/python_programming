<<<<<<< HEAD
patients=[]
n=int(input("Enter the number of patients"))
for i in range(n):
    name=input(f"Enter name for{i+1} patient")
    age=int(input("Enter the age"))
    disease=input("Enter the disease")
    patient={"Name":name ,"Age":age,"Disease":disease}
    patients.append(patient)
search_disease=input("Enter the disease name")
print("Patients with ",search_disease)
for patient in patients:
    if (search_disease==patient["Disease"]):
        print(patient["Name"])
=======
patients=[]
n=int(input("Enter the number of patients"))
for i in range(n):
    name=input(f"Enter name for{i+1} patient")
    age=int(input("Enter the age"))
    disease=input("Enter the disease")
    patient={"Name":name ,"Age":age,"Disease":disease}
    patients.append(patient)
search_disease=input("Enter the disease name")
for patient in patients:
    if (search_disease==patient[disease]):
        print(patient["Name"])
>>>>>>> 0fa6456496e9d71ee8c18890d9747d5bd6d029d0
