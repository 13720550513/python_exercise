import yaml 
import argparse

def getinput():
    parse=argparse.ArgumentParser(description='Welcome to this project')
    parse.add_argument('-y',required=True,help='please input a yaml_file')
    args=parse.parse_args()
    
    yamlfile=args.y
    con_file=open(yamlfile)
    fileload=yaml.full_load(con_file)
    a=fileload['a']
    b=fileload['b']
    return a,b

def getBig():
    a,b=getinput()
    if a>b:
        print('较大的是:{}'.format(a))
    elif a<b:
        print('较大的是:{}'.format(b))
    else:
        print('一样大')

def main():
    getBig()

main()
