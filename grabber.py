import requests, json
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
class Pausi(object):
        """docstring for Pausi"""
        def __init__(self, key, displays=''):
                self.url = 'http://104.42.122.163/api.php?key='+key
                if displays:self.displays = True
                else:self.displays = False
                self.save = open('weblist.txt', 'a')
                self.main()
        def main(self):
                req = requests.get(self.url)
                if req.status_code == 200 and req.text:
                        res = json.loads(req.text)
                        if res['msg']:
                                print res['msg']
                        else:
                                for x in res['urls']:
                                        if self.displays:print x
                                        else:pass
                                        self.save.write(x+'\n')
                                jum = len(res['urls'])
                                print "managed to get {} urls".format(jum)

class Main(object):
        """docstring for Main"""
        def __init__(self):
                self.main()
        def main(self):
                print '''
--- Coded by M!L3z ---
+++   MillerSec-ID  +++

1. Get Weblist
2. Remove Duplicate Sites
                '''
                inp = input('Select:: ')
                try:
                        if inp == 1:
                                se = raw_input("show all results? [Y/n]")
                                if se == 'Y' or se == 'y':disp = True
                                else:disp = False
                                threadss = input('Thread:: ')
                                print "your results will be saved in :: weblist.txt"
                                thr = []
                                for x in range(threadss):
                                        thr.append('public')
                                while True:
                                        pool = ThreadPool(len(thr))
                                        pool.map(Pausi, thr)
                                        pool.close()
                                        pool.join()
                                        #Pausi(key='public', displays=disp)
                        elif inp == 2:
                                self.remove_duplicate()
                except:
                        pass
        def remove_duplicate(self):
                tmp = []
                lists = raw_input('Your list: ')
                save = raw_input('Save Name: ')
                sv = open(save,'a')
                with open(lists) as fileobject:
                    for x in fileobject:
                        x = x.strip()
                        if x in tmp:
                                print x+" Duplicate Url"
                        else:
                                tmp.append(x)
                                sv.write(x+'\n')
                                print x+" OK"

Main()
