import shelve
db = shelve.open('persondb')

for k in sorted(db):
    print(k, '\t', db[k])

sue = db['Sue Jones']
sue.giveRaise(.10)
db['Sue Jones'] = sue
db.close()
