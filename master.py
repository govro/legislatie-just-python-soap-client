# Launches in parallel multiple instances of script.py

from subprocess import Popen
import argparse

parser = argparse.ArgumentParser(description='Benchmark legislatie.just.ro')
parser.add_argument("-n", "--num", dest="num",
                    help="NUM of processes to spawn", metavar="num", default=4)
parser.add_argument("-b", "--begin-at", dest="begin",
                    help="begin at page PAGE", metavar="PAGE", default=0)
parser.add_argument("-p", "--pages", dest="pages",
                    help="number of PAGES fetched by subprocess", metavar="PAGES", default=1000)

args = vars(parser.parse_args())

num = int(args['num'])
f = int(args['begin'])
pages = int(args['pages'])

process_list = []

print("==== Spawning {0} processes\n".format(num))

for i in range(num):
    to = f + pages

    p = Popen(['python3', 'script.py', '-n', str(f), '-N', str(to)])
    process_list.append(p)

    f = to

print("==== Waiting for processes to finish\n")

for i in range(num):
    ret = process_list[i].wait()
    print("==== Process {0} exited with status {1}\n".format(i, ret))

