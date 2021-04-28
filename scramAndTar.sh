# cd ~/CMSSW_10_2_22/src
# eval `scramv1 runtime -sh`
# source /home/users/mcitron/ProjectMetisForV7/ProjectMetis/setup.sh
# eval `scramv1 runtime -sh`
# scramv1 b -j 8
# mtarfile package.tar.xz --xz -e psets gridpacks
# cd -
# cp ~/CMSSW_10_2_22/src/package.tar.xz . 
tar -cJf package_2018.tar.xz psets gridpacks psets_gensim psets_gensim_noFilter -C ~/CMSSW_10_2_22/src/ JMEAnalysis cms_lpc_llp
tar -cJf package_2017.tar.xz psets gridpacks psets_gensim psets_gensim_noFilter -C ~/CMSSW_9_4_17/src/ JMEAnalysis cms_lpc_llp
tar -cJf package_2016.tar.xz psets gridpacks psets_gensim psets_gensim_noFilter -C ~/2016/CMSSW_9_4_17/src/ JMEAnalysis cms_lpc_llp
