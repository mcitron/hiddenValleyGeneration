import FWCore.ParameterSet.Config as cms

scoutingMuonCountFilter = cms.EDFilter('ScoutingMuonCountFilter',
  src = cms.InputTag(''),
  minNumber = cms.uint32(0)
)
