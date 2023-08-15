from insurance_classes import *

# Making objects by using for loop
persons = []
for i in range(int(input('Please enter the number of patients to be registered:'))):
    person = Patient(input(f"Enter the number {i+1} patient's name:"), int(input('His/her age in years:')),
    int(input('Sex code (0 = male, 1 = female):')),
    float(input('BMI in decimals:')), int(input('Number of children:')),
    int(input('Smoker status code (0 = non smoker, 1 = smoker):')))
    persons.append(person)
    
# Traversing persons and print every patient information and insurance cost by using patient_profile and estimated_insurace_cost methods.
for person in persons:
    print(f"\nPatient {person.name}'s profile information is below: {person.patient_profile()}")
    print(f"The estimated insurance cost is {person.estimated_insurance_cost()} dollars.\n")
if Patient.counter == 1:
    print(f'\nYou registered {Patient.counter} patient successfully.\n')
else:
    print(f'\nYou registered {Patient.counter} patients successfully.\n')

# Selecting one patient to use the update_age and estimated_insurance cost method to see "Inheritence".
requested_name = input("Enter the patient's name whose age must be updated:\n")
for person in persons:
    if requested_name == person.name:
        print(f"{person.name}'s updated age is {person.update_age(int(input('Enter current age:')), force=True)}.")
        print(f"The estimated insurance cost is {person.estimated_insurance_cost()} dollars.")
