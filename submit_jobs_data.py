from metis.CMSSWTask import CMSSWTask
from metis.CondorTask import CondorTask
from metis.Sample import DirectorySample, DBSSample, DummySample
from metis.StatsParser import StatsParser
from metis.Optimizer import Optimizer
import time

import itertools
import pandas as pd
def submit(which):
    total_summary = {}

    tag = "ZMuMuSkim_v0"
    task = CMSSWTask(
            sample = DBSSample(dataset="/SingleMuon/Run2017F-ZMu-17Nov2017-v1/RAW-RECO"),
            events_per_output = 10000,
            pset = "/home/users/mcitron/CMSSW_9_4_17/src/cms_lpc_llp/llp_ntupler/python/displacedJetMuon_ntupler_Data_2017_RAWRECO.py",
            cmssw_version = "CMSSW_9_4_17",
            scram_arch = "slc6_amd64_gcc700",
            tag = tag,
            # dont_check_tree = True,
            executable = "/home/users/mcitron/exeForMetis/condor_genprod_exe.sh",
            condor_submit_params = {
                "container": "/cvmfs/singularity.opensciencegrid.org/cmssw/cms:rhel6-m202006",
                },
            recopy_inputs=True
            )
    task.process()
    total_summary[task.get_sample().get_datasetname()] = task.get_task_summary()

    StatsParser(data=total_summary, webdir="~/public_html/dump/metis_test/").do()

if __name__ == "__main__":

    for i in range(500):
        # submit("hzdzd")
        submit("hv")
        time.sleep(2*60*60)

