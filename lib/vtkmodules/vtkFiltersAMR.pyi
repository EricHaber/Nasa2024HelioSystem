from typing import overload, Any, Callable, TypeVar, Union
from typing import Tuple, List, Sequence, MutableSequence

Callback = Union[Callable[..., None], None]
Buffer = TypeVar('Buffer')
Pointer = TypeVar('Pointer')
Template = TypeVar('Template')

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonExecutionModel

class vtkAMRCutPlane(vtkmodules.vtkCommonExecutionModel.vtkMultiBlockDataSetAlgorithm):
    def FillInputPortInformation(self, port:int, info:'vtkInformation') -> int: ...
    def FillOutputPortInformation(self, port:int, info:'vtkInformation') -> int: ...
    def GetController(self) -> 'vtkMultiProcessController': ...
    def GetLevelOfResolution(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetUseNativeCutter(self) -> bool: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkAMRCutPlane': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkAMRCutPlane': ...
    @overload
    def SetCenter(self, _arg1:float, _arg2:float, _arg3:float) -> None: ...
    @overload
    def SetCenter(self, _arg:Sequence[float]) -> None: ...
    def SetController(self, __a:'vtkMultiProcessController') -> None: ...
    def SetInitialRequest(self, _arg:bool) -> None: ...
    def SetLevelOfResolution(self, _arg:int) -> None: ...
    @overload
    def SetNormal(self, _arg1:float, _arg2:float, _arg3:float) -> None: ...
    @overload
    def SetNormal(self, _arg:Sequence[float]) -> None: ...
    def SetUseNativeCutter(self, _arg:bool) -> None: ...
    def UseNativeCutterOff(self) -> None: ...
    def UseNativeCutterOn(self) -> None: ...

class vtkAMRGaussianPulseSource(vtkmodules.vtkCommonExecutionModel.vtkOverlappingAMRAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetPulseAmplitude(self) -> float: ...
    def GetPulseOrigin(self) -> Tuple[float, float, float]: ...
    def GetPulseWidth(self) -> Tuple[float, float, float]: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkAMRGaussianPulseSource': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkAMRGaussianPulseSource': ...
    def SetDimension(self, _arg:int) -> None: ...
    def SetNumberOfLevels(self, _arg:int) -> None: ...
    def SetPulseAmplitude(self, _arg:float) -> None: ...
    @overload
    def SetPulseOrigin(self, _arg1:float, _arg2:float, _arg3:float) -> None: ...
    @overload
    def SetPulseOrigin(self, _arg:Sequence[float]) -> None: ...
    @overload
    def SetPulseWidth(self, _arg1:float, _arg2:float, _arg3:float) -> None: ...
    @overload
    def SetPulseWidth(self, _arg:Sequence[float]) -> None: ...
    def SetRefinementRatio(self, r:int) -> None: ...
    def SetRootSpacing(self, h0:float) -> None: ...
    def SetXPulseOrigin(self, f:float) -> None: ...
    def SetXPulseWidth(self, f:float) -> None: ...
    def SetYPulseOrigin(self, f:float) -> None: ...
    def SetYPulseWidth(self, f:float) -> None: ...
    def SetZPulseOrigin(self, f:float) -> None: ...
    def SetZPulseWidth(self, f:float) -> None: ...

class vtkAMRResampleFilter(vtkmodules.vtkCommonExecutionModel.vtkMultiBlockDataSetAlgorithm):
    def FillInputPortInformation(self, port:int, info:'vtkInformation') -> int: ...
    def FillOutputPortInformation(self, port:int, info:'vtkInformation') -> int: ...
    def GetBiasVector(self) -> Tuple[float, float, float]: ...
    def GetController(self) -> 'vtkMultiProcessController': ...
    def GetDemandDrivenMode(self) -> int: ...
    def GetMax(self) -> Tuple[float, float, float]: ...
    def GetMin(self) -> Tuple[float, float, float]: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetNumberOfPartitions(self) -> int: ...
    def GetNumberOfSamples(self) -> Tuple[int, int, int]: ...
    def GetTransferToNodes(self) -> int: ...
    def GetUseBiasVector(self) -> bool: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkAMRResampleFilter': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkAMRResampleFilter': ...
    @overload
    def SetBiasVector(self, _arg1:float, _arg2:float, _arg3:float) -> None: ...
    @overload
    def SetBiasVector(self, _arg:Sequence[float]) -> None: ...
    def SetController(self, __a:'vtkMultiProcessController') -> None: ...
    def SetDemandDrivenMode(self, _arg:int) -> None: ...
    @overload
    def SetMax(self, _arg1:float, _arg2:float, _arg3:float) -> None: ...
    @overload
    def SetMax(self, _arg:Sequence[float]) -> None: ...
    @overload
    def SetMin(self, _arg1:float, _arg2:float, _arg3:float) -> None: ...
    @overload
    def SetMin(self, _arg:Sequence[float]) -> None: ...
    def SetNumberOfPartitions(self, _arg:int) -> None: ...
    @overload
    def SetNumberOfSamples(self, _arg1:int, _arg2:int, _arg3:int) -> None: ...
    @overload
    def SetNumberOfSamples(self, _arg:Sequence[int]) -> None: ...
    def SetTransferToNodes(self, _arg:int) -> None: ...
    def SetUseBiasVector(self, _arg:bool) -> None: ...

class vtkAMRSliceFilter(vtkmodules.vtkCommonExecutionModel.vtkOverlappingAMRAlgorithm):
    class NormalTag(int): ...
    X_NORMAL:'NormalTag'
    Y_NORMAL:'NormalTag'
    Z_NORMAL:'NormalTag'
    def FillInputPortInformation(self, port:int, info:'vtkInformation') -> int: ...
    def FillOutputPortInformation(self, port:int, info:'vtkInformation') -> int: ...
    def GetController(self) -> 'vtkMultiProcessController': ...
    def GetMaxResolution(self) -> int: ...
    def GetNormal(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetOffsetFromOrigin(self) -> float: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkAMRSliceFilter': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkAMRSliceFilter': ...
    def SetController(self, __a:'vtkMultiProcessController') -> None: ...
    def SetMaxResolution(self, _arg:int) -> None: ...
    def SetNormal(self, _arg:int) -> None: ...
    def SetOffsetFromOrigin(self, _arg:float) -> None: ...

class vtkAMRToMultiBlockFilter(vtkmodules.vtkCommonExecutionModel.vtkMultiBlockDataSetAlgorithm):
    def FillInputPortInformation(self, port:int, info:'vtkInformation') -> int: ...
    def FillOutputPortInformation(self, port:int, info:'vtkInformation') -> int: ...
    def GetController(self) -> 'vtkMultiProcessController': ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkAMRToMultiBlockFilter': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkAMRToMultiBlockFilter': ...
    def SetController(self, __a:'vtkMultiProcessController') -> None: ...

class vtkImageToAMR(vtkmodules.vtkCommonExecutionModel.vtkOverlappingAMRAlgorithm):
    def GetMaximumNumberOfBlocks(self) -> int: ...
    def GetMaximumNumberOfBlocksMaxValue(self) -> int: ...
    def GetMaximumNumberOfBlocksMinValue(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetNumberOfLevels(self) -> int: ...
    def GetNumberOfLevelsMaxValue(self) -> int: ...
    def GetNumberOfLevelsMinValue(self) -> int: ...
    def GetRefinementRatio(self) -> int: ...
    def GetRefinementRatioMaxValue(self) -> int: ...
    def GetRefinementRatioMinValue(self) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkImageToAMR': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkImageToAMR': ...
    def SetMaximumNumberOfBlocks(self, _arg:int) -> None: ...
    def SetNumberOfLevels(self, _arg:int) -> None: ...
    def SetRefinementRatio(self, _arg:int) -> None: ...

class vtkParallelAMRUtilities(vtkmodules.vtkCommonDataModel.vtkAMRUtilities):
    @staticmethod
    def BlankCells(amr:'vtkOverlappingAMR', myController:'vtkMultiProcessController') -> None: ...
    @staticmethod
    def DistributeProcessInformation(amr:'vtkOverlappingAMR', myController:'vtkMultiProcessController', ProcessMap:MutableSequence[int]) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkParallelAMRUtilities': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkParallelAMRUtilities': ...
    @staticmethod
    def StripGhostLayers(ghostedAMRData:'vtkOverlappingAMR', strippedAMRData:'vtkOverlappingAMR', myController:'vtkMultiProcessController') -> None: ...

