# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuffers

import flatbuffers

class TextOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsTextOptions(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TextOptions()
        x.Init(buf, n + offset)
        return x

    # TextOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TextOptions
    def WidgetOptions(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .WidgetOptions import WidgetOptions
            obj = WidgetOptions()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # TextOptions
    def FontResource(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .ResourceData import ResourceData
            obj = ResourceData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # TextOptions
    def FontName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TextOptions
    def FontSize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # TextOptions
    def Text(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TextOptions
    def AreaWidth(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # TextOptions
    def AreaHeight(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # TextOptions
    def HAlignment(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # TextOptions
    def VAlignment(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # TextOptions
    def TouchScaleEnable(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # TextOptions
    def IsCustomSize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # TextOptions
    def OutlineEnabled(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # TextOptions
    def OutlineColor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            x = o + self._tab.Pos
            from .Color import Color
            obj = Color()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # TextOptions
    def OutlineSize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 1

    # TextOptions
    def ShadowEnabled(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # TextOptions
    def ShadowColor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            x = o + self._tab.Pos
            from .Color import Color
            obj = Color()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # TextOptions
    def ShadowOffsetX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 2.0

    # TextOptions
    def ShadowOffsetY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return -2.0

    # TextOptions
    def ShadowBlurRadius(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # TextOptions
    def IsLocalized(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def TextOptionsStart(builder): builder.StartObject(20)
def TextOptionsAddWidgetOptions(builder, widgetOptions): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(widgetOptions), 0)
def TextOptionsAddFontResource(builder, fontResource): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(fontResource), 0)
def TextOptionsAddFontName(builder, fontName): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(fontName), 0)
def TextOptionsAddFontSize(builder, fontSize): builder.PrependInt32Slot(3, fontSize, 0)
def TextOptionsAddText(builder, text): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(text), 0)
def TextOptionsAddAreaWidth(builder, areaWidth): builder.PrependInt32Slot(5, areaWidth, 0)
def TextOptionsAddAreaHeight(builder, areaHeight): builder.PrependInt32Slot(6, areaHeight, 0)
def TextOptionsAddHAlignment(builder, hAlignment): builder.PrependInt32Slot(7, hAlignment, 0)
def TextOptionsAddVAlignment(builder, vAlignment): builder.PrependInt32Slot(8, vAlignment, 0)
def TextOptionsAddTouchScaleEnable(builder, touchScaleEnable): builder.PrependBoolSlot(9, touchScaleEnable, 0)
def TextOptionsAddIsCustomSize(builder, isCustomSize): builder.PrependBoolSlot(10, isCustomSize, 0)
def TextOptionsAddOutlineEnabled(builder, outlineEnabled): builder.PrependBoolSlot(11, outlineEnabled, 0)
def TextOptionsAddOutlineColor(builder, outlineColor): builder.PrependStructSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(outlineColor), 0)
def TextOptionsAddOutlineSize(builder, outlineSize): builder.PrependInt32Slot(13, outlineSize, 1)
def TextOptionsAddShadowEnabled(builder, shadowEnabled): builder.PrependBoolSlot(14, shadowEnabled, 0)
def TextOptionsAddShadowColor(builder, shadowColor): builder.PrependStructSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(shadowColor), 0)
def TextOptionsAddShadowOffsetX(builder, shadowOffsetX): builder.PrependFloat32Slot(16, shadowOffsetX, 2.0)
def TextOptionsAddShadowOffsetY(builder, shadowOffsetY): builder.PrependFloat32Slot(17, shadowOffsetY, -2.0)
def TextOptionsAddShadowBlurRadius(builder, shadowBlurRadius): builder.PrependInt32Slot(18, shadowBlurRadius, 0)
def TextOptionsAddIsLocalized(builder, isLocalized): builder.PrependBoolSlot(19, isLocalized, 0)
def TextOptionsEnd(builder): return builder.EndObject()