import FWCore.ParameterSet.Config as cms

scoutingVertexCountFilter = cms.EDFilter('ScoutingVertexCountFilter',
  src = cms.InputTag(''),
  minNumber = cms.uint32(0)
)
