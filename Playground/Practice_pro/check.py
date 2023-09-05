class Patient:
    patient_counter = 0

    def __init__(self, name: str, age: int, sex: int, bmi: float, num_child: int, smok_stat: int) -> None:
        
        self.name = name
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.num_child = num_child
        self.smok_stat = smok_stat
        patient_counter +=1

        
    def ins_cost(self) -> int:
        return 250*self.age + 128*self.age + 370*self.bmi + 24000*self.num_child + 12000*self.smok_stat
    
    def profile(self) -> dict:
        return {'name':self.name,
                'age':self.age,
                'sex':self.sex,
                'bmi':self.bmi,
                'num_of_children:':self.num_child,
                'smoker':self.smok_stat}
        
    def update_age(self, new_age: int) -> int:
        self.age = new_age
        return self.age
    
    def update_bmi(self, new_bmi: float) -> float:
        self.bmi = new_bmi
        return self.bmi
    
    def update_num_child(self, new_child: int) -> int:
        self.num_child = new_child
        return self.num_child
    
    def update_smok_stat(self, smoker: object) -> int:
        if smoker in [True, 'Yes', 1]:
            self.smoker = 1
        elif smoker in [False, 'No', 0]:
            self.smoker = 0
        return self.smoker


persons = [Patient(input('Name:'), int(input('Age:')), input('Sex:'), float(input('BMI:')), int(input('Number of children')), int(input('Smoker status:')))
for _ in range(int(input('Number of patients to be registered:')))]

for patient in persons:
    print(f'Profile: {patient.profile()}')
    print(f'The estimates insurance cost of {patient.name} is ${int(patient.ins_cost()):,}')

        
