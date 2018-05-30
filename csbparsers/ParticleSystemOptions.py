# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuffers

import flatbuffers

class ParticleSystemOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsParticleSystemOptions(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ParticleSystemOptions()
        x.Init(buf, n + offset)
        return x

    # ParticleSystemOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ParticleSystemOptions
    def NodeOptions(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .WidgetOptions import WidgetOptions
            obj = WidgetOptions()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ParticleSystemOptions
    def FileNameData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .ResourceData import ResourceData
            obj = ResourceData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ParticleSystemOptions
    def BlendFunc(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = o + self._tab.Pos
            from .BlendFunc import BlendFunc
            obj = BlendFunc()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def ParticleSystemOptionsStart(builder): builder.StartObject(3)
def ParticleSystemOptionsAddNodeOptions(builder, nodeOptions): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(nodeOptions), 0)
def ParticleSystemOptionsAddFileNameData(builder, fileNameData): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(fileNameData), 0)
def ParticleSystemOptionsAddBlendFunc(builder, blendFunc): builder.PrependStructSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(blendFunc), 0)
def ParticleSystemOptionsEnd(builder): return builder.EndObject()
