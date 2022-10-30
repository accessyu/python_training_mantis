from model.project import Project
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of projects", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 10
f = "data/project.json"

for o, a in opts:
   if o == "-n":
       n = int(a)
   elif o == "-f":
       f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*5
    return prefix + "".join(filter(lambda x: x != "'",
                                    filter(lambda x: x != "  ",
                                        filter(lambda x: x is not None,
                                               [random.choice(symbols) for i in range(random.randrange(maxlen))]))))

status = ['development', 'release', 'stable', 'obsolete']
is_inherited = [True, False]
view_status = ['public', 'private']

testdata = [Project(project_name=random_string('name', 7), status=random.choice(status),
                    is_inherited = random.choice(is_inherited), view_status=random.choice(view_status), \
                    desc=random_string('description', 7))
            for i in range(1)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as output:
    jsonpickle.set_encoder_options("json", indent=2)
    output.write(jsonpickle.encode(testdata))