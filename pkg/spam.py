# import string - this will skip search in the package and start making absolute import from Python lib.
from . import string # this however will search in the package meaning this is a relative import.
print(string)