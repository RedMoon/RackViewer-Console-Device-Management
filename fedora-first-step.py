import argparse

parser = argparse.ArgumentParser(description='Tar watcher')
parser.add_argument('a', type=str, help='Input dir for videos')
args = parser.parse_args()
print(args.a)

