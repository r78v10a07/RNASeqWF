import os
import re
import json
import pandas
import math
import pickle
import zipfile
import numpy as np
import scipy.stats as stats
import seaborn as sns

from IPython.display import display

import matplotlib
import matplotlib.pyplot as plt

from IPython.display import HTML
from IPython.display import display, Markdown, Latex

###############################################################
#
#    Update this path
#
###############################################################
os.environ['WORKDIR'] = os.path.abspath('/gfs/projects/RNASeqWF')
###############################################################

os.environ['CONFIG'] = os.environ['WORKDIR'] + '/config'
os.environ['DATA'] = os.environ['WORKDIR'] + '/data'
os.environ['BIN'] = os.environ['WORKDIR'] + '/bin'
os.environ['RESULTS'] = os.environ['WORKDIR'] + '/results'
os.environ['NOTEBOOKS'] = os.environ['WORKDIR'] + '/notebooks'
os.environ['SRC'] = os.environ['WORKDIR'] + '/src'
os.environ['TMP'] = os.environ['WORKDIR'] + '/tmp'
os.environ['CWLTOOLS'] = os.environ['BIN'] + '/cwl-workflow/tools'
os.environ['CWLWORKFLOWS'] = os.environ['BIN'] + '/cwl-workflow/workflows'

os.environ['DATASET'] = 'PRJNA339968'

HIDE_CODE = '''<script>
code_show=true; 
function code_toggle() {
 if (code_show){
 $('div.input').hide();
 } else {
 $('div.input').show();
 }
 code_show = !code_show
} 
$( document ).ready(code_toggle);
</script>
The raw code for this IPython notebook is by default hidden for easier reading.
To toggle on/off the raw code, click <a href="javascript:code_toggle()">here</a>.'''

def parse_fastqc_zip(sample, zip_file):
    tests = {}
    tot_seq = 0
    poor_quality = 0
    seq_len = ''
    gc_content = ''
    if os.path.exists(zip_file):        
        with zipfile.ZipFile(zip_file) as myzip:
            with myzip.open(sample + '_fastqc/summary.txt') as myfile:
                for line in myfile:
                    fields = line.strip().decode('utf8').split('\t')
                    tests[fields[1]] = fields[0]
            with myzip.open(sample + '_fastqc/fastqc_data.txt') as myfile:
                for line in myfile:
                    fields = line.strip().decode('utf8').split('\t')
                    if fields[0] == 'Total Sequences':
                        tot_seq = int(fields[1])
                    if fields[0] == 'Sequences flagged as poor quality':
                        poor_quality = int(fields[1])
                    if fields[0] == 'Sequence length':
                        seq_len = fields[1]
                    if fields[0] == '%GC':
                        gc_content = fields[1]
    return tests, tot_seq, poor_quality, seq_len, gc_content
    
