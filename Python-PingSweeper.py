#! /usr/bin/env python
# author: op.
'''
create short ping sweep script of your local subnet using a higher level
programming language such as Python, Ruby or Perl.
'''

from multiprocessing import Pool
import subprocess as sub

def ping(ip):
    out = sub.Popen(['ping', '-w1', '-c1', ip], stdout=sub.PIPE).communicate()[0]
    if 'ttl' in out:
        print('{} is up.'.format(ip))

def main():
  '''
  larger pool size makes this script run faster. size of 4p, script runs over 1min long
  size of 8p, abt 30s, 16p = abt 16s, 32p = abt 8s, 128p = abt 2s
  need to research more multiprocessing module.
  '''
    pool = Pool(128) 
    ips = ['192.168.1.{}'.format(i) for i in xrange(1,255)]
    pool.map(ping, ips)
    pool.close()
    pool.join()

if __name__ == '__main__':
  main()
