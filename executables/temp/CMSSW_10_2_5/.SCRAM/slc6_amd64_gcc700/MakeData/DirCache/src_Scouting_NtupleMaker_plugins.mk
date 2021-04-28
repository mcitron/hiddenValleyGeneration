ifeq ($(strip $(ScoutingTreeProducerPlugins)),)
ScoutingTreeProducerPlugins := self/src/Scouting/NtupleMaker/plugins
PLUGINS:=yes
ScoutingTreeProducerPlugins_files := $(patsubst src/Scouting/NtupleMaker/plugins/%,%,$(foreach file,*.cc,$(eval xfile:=$(wildcard src/Scouting/NtupleMaker/plugins/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/Scouting/NtupleMaker/plugins/$(file). Please fix src/Scouting/NtupleMaker/plugins/BuildFile.))))
ScoutingTreeProducerPlugins_BuildFile    := $(WORKINGDIR)/cache/bf/src/Scouting/NtupleMaker/plugins/BuildFile
ScoutingTreeProducerPlugins_LOC_USE := self  root rootrflx rootcore JetMETCorrections/Algorithms RecoJets/JetAlgorithms DataFormats/JetReco DataFormats/VertexReco DataFormats/Candidate DataFormats/PatCandidates DataFormats/Common DataFormats/HLTReco PhysicsTools/UtilAlgos FWCore/Framework FWCore/PluginManager FWCore/ServiceRegistry HLTrigger/HLTcore L1Trigger/L1TGlobal CondFormats/DataRecord
ScoutingTreeProducerPlugins_PRE_INIT_FUNC += $$(eval $$(call edmPlugin,ScoutingTreeProducerPlugins,ScoutingTreeProducerPlugins,$(SCRAMSTORENAME_LIB),src/Scouting/NtupleMaker/plugins))
ScoutingTreeProducerPlugins_PACKAGE := self/src/Scouting/NtupleMaker/plugins
ALL_PRODS += ScoutingTreeProducerPlugins
Scouting/NtupleMaker_forbigobj+=ScoutingTreeProducerPlugins
ScoutingTreeProducerPlugins_INIT_FUNC        += $$(eval $$(call Library,ScoutingTreeProducerPlugins,src/Scouting/NtupleMaker/plugins,src_Scouting_NtupleMaker_plugins,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_LIB),$(SCRAMSTORENAME_LOGS)))
ScoutingTreeProducerPlugins_CLASS := LIBRARY
else
$(eval $(call MultipleWarningMsg,ScoutingTreeProducerPlugins,src/Scouting/NtupleMaker/plugins))
endif
ALL_COMMONRULES += src_Scouting_NtupleMaker_plugins
src_Scouting_NtupleMaker_plugins_parent := Scouting/NtupleMaker
src_Scouting_NtupleMaker_plugins_INIT_FUNC += $$(eval $$(call CommonProductRules,src_Scouting_NtupleMaker_plugins,src/Scouting/NtupleMaker/plugins,PLUGINS))
