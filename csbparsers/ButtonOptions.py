# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuffers

import flatbuffers

class ButtonOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsButtonOptions(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ButtonOptions()
        x.Init(buf, n + offset)
        return x

    # ButtonOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ButtonOptions
    def WidgetOptions(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .WidgetOptions import WidgetOptions
            obj = WidgetOptions()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ButtonOptions
    def NormalData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .ResourceData import ResourceData
            obj = ResourceData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ButtonOptions
    def PressedData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .ResourceData import ResourceData
            obj = ResourceData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ButtonOptions
    def DisabledData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .ResourceData import ResourceData
            obj = ResourceData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ButtonOptions
    def FontResource(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .ResourceData import ResourceData
            obj = ResourceData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ButtonOptions
    def Text(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ButtonOptions
    def IsLocalized(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # ButtonOptions
    def FontName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ButtonOptions
    def FontSize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ButtonOptions
    def TextColor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            x = o + self._tab.Pos
            from .Color import Color
            obj = Color()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ButtonOptions
    def CapInsets(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            x = o + self._tab.Pos
            from .CapInsets import CapInsets
            obj = CapInsets()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ButtonOptions
    def Scale9Size(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            x = o + self._tab.Pos
            from .FlatSize import FlatSize
            obj = FlatSize()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ButtonOptions
    def Scale9Enabled(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # ButtonOptions
    def Displaystate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # ButtonOptions
    def OutlineEnabled(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # ButtonOptions
    def OutlineColor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            x = o + self._tab.Pos
            from .Color import Color
            obj = Color()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ButtonOptions
    def OutlineSize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 1

    # ButtonOptions
    def ShadowEnabled(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # ButtonOptions
    def ShadowColor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            x = o + self._tab.Pos
            from .Color import Color
            obj = Color()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ButtonOptions
    def ShadowOffsetX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 2.0

    # ButtonOptions
    def ShadowOffsetY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return -2.0

    # ButtonOptions
    def ShadowBlurRadius(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def ButtonOptionsStart(builder): builder.StartObject(22)
def ButtonOptionsAddWidgetOptions(builder, widgetOptions): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(widgetOptions), 0)
def ButtonOptionsAddNormalData(builder, normalData): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(normalData), 0)
def ButtonOptionsAddPressedData(builder, pressedData): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(pressedData), 0)
def ButtonOptionsAddDisabledData(builder, disabledData): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(disabledData), 0)
def ButtonOptionsAddFontResource(builder, fontResource): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(fontResource), 0)
def ButtonOptionsAddText(builder, text): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(text), 0)
def ButtonOptionsAddIsLocalized(builder, isLocalized): builder.PrependBoolSlot(6, isLocalized, 0)
def ButtonOptionsAddFontName(builder, fontName): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(fontName), 0)
def ButtonOptionsAddFontSize(builder, fontSize): builder.PrependInt32Slot(8, fontSize, 0)
def ButtonOptionsAddTextColor(builder, textColor): builder.PrependStructSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(textColor), 0)
def ButtonOptionsAddCapInsets(builder, capInsets): builder.PrependStructSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(capInsets), 0)
def ButtonOptionsAddScale9Size(builder, scale9Size): builder.PrependStructSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(scale9Size), 0)
def ButtonOptionsAddScale9Enabled(builder, scale9Enabled): builder.PrependBoolSlot(12, scale9Enabled, 0)
def ButtonOptionsAddDisplaystate(builder, displaystate): builder.PrependBoolSlot(13, displaystate, 1)
def ButtonOptionsAddOutlineEnabled(builder, outlineEnabled): builder.PrependBoolSlot(14, outlineEnabled, 0)
def ButtonOptionsAddOutlineColor(builder, outlineColor): builder.PrependStructSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(outlineColor), 0)
def ButtonOptionsAddOutlineSize(builder, outlineSize): builder.PrependInt32Slot(16, outlineSize, 1)
def ButtonOptionsAddShadowEnabled(builder, shadowEnabled): builder.PrependBoolSlot(17, shadowEnabled, 0)
def ButtonOptionsAddShadowColor(builder, shadowColor): builder.PrependStructSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(shadowColor), 0)
def ButtonOptionsAddShadowOffsetX(builder, shadowOffsetX): builder.PrependFloat32Slot(19, shadowOffsetX, 2.0)
def ButtonOptionsAddShadowOffsetY(builder, shadowOffsetY): builder.PrependFloat32Slot(20, shadowOffsetY, -2.0)
def ButtonOptionsAddShadowBlurRadius(builder, shadowBlurRadius): builder.PrependInt32Slot(21, shadowBlurRadius, 0)
def ButtonOptionsEnd(builder): return builder.EndObject()
