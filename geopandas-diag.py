"""
geopandas-diag.py
Apr 2023 PJW

Check the setup of Anaconda to see what might be interfering
with a geopandas installation.

Under Windows this should be run from an Anaconda Prompt. Under 
macOS it should be run from a Terminal window. In either case, the 
command is:

   python geopandas-diag.py

It will produce a file called geopandas-diag.log with a lot of 
diagnostics. Please send that file to me via Slack.
"""

import subprocess

#
#  Function for running conda commands and capturing the output
#

def run_conda(cmd,ofh):
    proc = subprocess.run(['conda']+cmd.split(),
                          check=True,
                          capture_output=True,
                          text=True)
    ofh.writelines([f'Output from {cmd}:\n\n'])
    ofh.writelines(proc.stdout)
    ofh.writelines('\n')

#
#  Where to write the output
#

ofile = 'geopandas-diag.log'

#
#  Now open the log file and get to work
#

fh = open(ofile,'w')

run_conda('info',fh)
run_conda('clean -a -y',fh)
run_conda('list',fh)

#
#  Done
#

fh.close()
print('Output written to',ofile)
