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

    extra_requirements = "true"

    tag = "v0_noFilter"
    pdname = "HVNoFilter"
    events_per_point = int(1E4)
    events_per_job = int(100)
    cfgsDir = "psets_gensim_noFilter/"
    modelsFile = cfgsDir+"/models.txt"
    df = pd.read_csv(modelsFile)
    for year in ["2016","2017","2018"]:
        for iterr,row in df.iterrows():

            # fmass = float(mass)
            # mass = str(mass).replace(".","p")

            epp = int(events_per_point)

            reqname = "noFilter_m{}{}_ctau{}_xi_{}_{}_{}".format(row.portal,row.mass,row.ctau,row.xi,tag,year)
            njobs = epp//events_per_job
            sample = DummySample(dataset="/{}/params_{}_m_{}_ctau_{}mm_xi_{}_{}/LLPNTUPLE".format(pdname,row.portal,row.mass,row.ctau*10,row.xi,year),N=njobs,nevents=epp)
            task = CondorTask(
                    sample = sample,
                    output_name = "output.root",
                    executable = "executables/condor_executable_{}.sh".format(which),
                    tarfile = "package_{}.tar.xz".format(year),
                    open_dataset = True,
                    files_per_output = 1,
                    condor_submit_params = {
                        "classads": [
                            ["param_mass",row.mass],
                            ["param_ctau",row.ctau],
                            ["param_xi",str(row.xi).replace(".","p")],
                            ["param_portal",row.portal],
                            ["param_year",year],
                            ["param_nevents",events_per_job],
                            ["metis_extraargs",""],
                            ["JobBatchName",reqname],
                            ],
                        "requirements_line": 'Requirements = ((HAS_SINGULARITY=?=True) && (HAS_CVMFS_cms_cern_ch =?= true) && {extra_requirements})'.format(extra_requirements=extra_requirements),
                        },
                    tag = tag,
                    recopy_inputs = True
                    )
            task.process()
            total_summary[task.get_sample().get_datasetname()] = task.get_task_summary()

    StatsParser(data=total_summary, webdir="~/public_html/dump/metis_test/").do()

if __name__ == "__main__":

    for i in range(500):
        # submit("hzdzd")
        submit("hv_keepGenSim")
        time.sleep(2*60*60)

