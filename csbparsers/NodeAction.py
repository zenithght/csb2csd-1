# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuffers

import flatbuffers

class NodeAction(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsNodeAction(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = NodeAction()
        x.Init(buf, n + offset)
        return x

    # NodeAction
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # NodeAction
    def Duration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # NodeAction
    def Speed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # NodeAction
    def TimeLines(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .TimeLine import TimeLine
            obj = TimeLine()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # NodeAction
    def TimeLinesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # NodeAction
    def CurrentAnimationName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def NodeActionStart(builder): builder.StartObject(4)
def NodeActionAddDuration(builder, duration): builder.PrependInt32Slot(0, duration, 0)
def NodeActionAddSpeed(builder, speed): builder.PrependFloat32Slot(1, speed, 0.0)
def NodeActionAddTimeLines(builder, timeLines): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(timeLines), 0)
def NodeActionStartTimeLinesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def NodeActionAddCurrentAnimationName(builder, currentAnimationName): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(currentAnimationName), 0)
def NodeActionEnd(builder): return builder.EndObject()
