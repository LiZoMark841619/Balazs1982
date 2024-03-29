from person import Person, Manager
import shelve

bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=100000)
tom = Manager('Tom Jones', 50000)

db = shelve.open('persondb')
for object in (bob, sue, tom):
    db[object.name] = object
db.close()

