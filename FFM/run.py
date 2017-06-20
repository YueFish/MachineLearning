#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import subprocess, sys, os, time
NR_THREAD=1

start = time.time()

cmd = './utils/washDataDeleteIndex.py falseLabel_item_yu.csv falsesLabel_item_wash.csv'
subprocess.call(cmd, shell = True)

cmd = './utils/washDataDelteRepeat.py falsesLabel_item_wash falseLabel_item_washAndDelRe.csv'
subprocess.call(cmd, shell = True)

cmd = './utils/ cutData.py falseLabel_item_washAndDelRe.csv test.csv'
subprocess.call(cmd, shell = True)

cmd ='converters/predic-a.py test.csv all_item_tr.csv '
subprocess.call(cmd, shell = True)

cmd ='converters/predic-b.py all_item_tr.csv all_item_num_tr.txt'
subprocess.call(cmd, shell = True)

cmd ='rm -f falsesLabel_item_wash.csv falseLabel_item_washAndDelRe.csv test.csv all_item_tr.csv'
subprocess.call(cmd, shell = True)

cmd = 'converters/randomreadfile.py  all_item_num_tr.txt all_item_random_tr.txt'
subprocess.call(cmd, shell = True)

cmd = 'convertesr/cutdata.py all_item_random_tr.txt all_item_random_pr.txt all_item_random_te.txt all_item_random.tr.txt'

cmd = './ffm-train -k 4 -t 18 -s {nr_thread} -p all_item_random_te.txt all_item_random.tr.txt model'.format(nr_thread=NR_THREAD)
subprocess.call(cmd, shell=True)

cmd = './ffm-predict all_item_random_pr.txt model pr.out'.format(nr_thread=NR_THREAD)
subprocess.call(cmd, shell=True)

cmd = './utils/calucuteAuc.py pr.out pr.out.cal'
subprocess.call(cmd, shell=True)

print('time used = {0:.0f}'.format(time.time()-start))



