# Making a "Patient class".
class Patient:
    
# Making a class attribute to counter the registered patients.
    counter = 0
    
# Making an instantiation method in order to determine the object parameters.
    def __init__(self, name, age, sex, bmi, num_of_children, smoker):
        self.name = name
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.num_of_children = num_of_children
        self.smoker = smoker
        Patient.counter +=1
        
# Making object methods (how to estimate insurance cost, update age, number of children, bmi, smoking status)
    def estimated_insurance_cost(self):
        estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
        print(f"{self.name}'s estimated insurance cost is {int(estimated_cost)} dollars.")
    
    def update_age(self, new_age):
        self.age = new_age
        print(f"{self.name} is now {self.age} years old.")
    
    def update_num_children(self, new_num_children):
        self.num_of_children = new_num_children
        if self.num_of_children == 1:
            print(f"{self.name} has {self.num_of_children} child.")
        else:
            print(f"{self.name} has {self.num_of_children} children.")
    
    def patient_profile(self):
        self.patient_information = {
            'name':self.name,
            'age':self.age,
            'sex':self.sex,
            'bmi':self.bmi,
            'number of children':self.num_of_children,
            'smoker': self.smoker
        }
        print(f"\n{self.name}'s patient profile is {self.patient_information}")
    
    def update_bmi(self, new_bmi):
        if new_bmi not in [True, False]:
            try:
                self.bmi = float(new_bmi)
                print(f"{self.name}'s new BMI is {self.bmi}.")
            except:
                print('BMI cannot be string. Please enter a valid (0 for being a non smoker or 1 otherweise) value!')
        else:
            print('BMI cannot be True, or False. Please enter a valid (0 for being a non smoker or 1 otherweise) value!')
        
    def update_smoking_status(self, new_status):
        if new_status in ['Yes', True, 1]:
            self.smoker = 1
            print(f"{self.name} does smoke now and the status is {self.smoker}.")
        elif new_status in ['No', False, 0]:
            self.smoker = 0
            print(f"{self.name} does not smoke now and the status is {self.smoker}.")
            
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
    person.patient_profile(), person.estimated_insurance_cost()

print(f'\nThere are {Patient.counter} patients registered.\n')

# Selecting one patient to use the update_age and estimated_insurance cost method to see "Inheritence".
requested_name = input("Enter the patient's name whose age must be updated:\n")
for person in persons:
    if requested_name == person.name:
        person.update_age(int(input('Enter current age:')))
        person.estimated_insurance_cost()