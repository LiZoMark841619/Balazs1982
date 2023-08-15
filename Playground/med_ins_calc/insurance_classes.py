# Making a "Patient class".
class Patient:
# Making a class attribute to counter the registered patients.
    counter = 0
# Making an instantiation method in order to determine the object parameters.
    def __init__(self, name: str, age: int, sex: int, bmi: float, num_of_children: int, smoker: int) -> None:
        self.name = name
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.num_of_children = num_of_children
        self.smoker = smoker
        Patient.counter +=1  
# Making object methods (how to estimate insurance cost, update age, number of children, bmi, smoking status)
    def estimated_insurance_cost(self) -> float:
        estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
        return int(estimated_cost)
    
    def update_age(self, new_age: int) -> int:
        self.age = new_age
        return self.age
    
    def update_num_children(self, new_num_children) -> int:
        self.num_of_children = new_num_children
        return self.num_of_children

    def patient_profile(self) -> dict:
        self.patient_information = {
            'name':self.name,
            'age':self.age,
            'sex':self.sex,
            'bmi':self.bmi,
            'number of children':self.num_of_children,
            'smoker': self.smoker
        }
        return self.patient_information
    
    def update_bmi(self, new_bmi) -> float:
        if new_bmi not in [True, False]:
            try:
                self.bmi = float(new_bmi)
                return self.bmi
            except:
                print('BMI cannot be string. Please enter a valid (0 for being a non smoker or 1 otherweise) value!')
        
    def update_smoking_status(self, new_status) -> int:
        if new_status in ['Yes', True, 1]:
            self.smoker = 1
        elif new_status in ['No', False, 0]:
            self.smoker = 0
        return self.smoker