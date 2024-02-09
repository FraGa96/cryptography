import sys
import argparse
import hashlib

hashSha256 = lambda _string: hashlib.sha256(_string.encode('utf-8')).hexdigest()

hashSha512 = lambda _string: hashlib.sha512(_string.encode('utf-8')).hexdigest()

hashMd5 = lambda _string: hashlib.md5(_string.encode('utf-8')).hexdigest()

sha256 = 'sha256'
sha512 = 'sha512'
md5 = 'md5'

parser = argparse.ArgumentParser(description='Prints hashed password')
parser.add_argument('password')
parser.add_argument('-t', '--type', choices=[sha256, sha512, md5], default=sha256)

def main(args):
    if(args.type == sha256):
        print(hashSha256(args.password))
    elif(args.type == sha512):
        print(hashSha512(args.password))
    elif(args.type == md5):
        print(hashMd5(args.password))

if __name__ == '__main__':
    sys.exit(main(parser.parse_args()))
    