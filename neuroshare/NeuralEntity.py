from Entity import *

class NeuralEntity(Entity):
    def __init__(self, nsfile, eid, info):
        super(NeuralEntity,self).__init__(eid, nsfile, info)

    @property
    def probe_info(self):
        return self._info['ProbeInfo']

    @property
    def source_entity_id(self):
	return self._info['SourceEntityID']

    @property
    def source_unit_id(self):
        return self._info['SourceUnitID']
        
    def get_data (self, index, count):
        lib = self.file.library
        data = lib._get_neural_data (self, index, count)
        return data
