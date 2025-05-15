from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OperationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    InOperation: _ClassVar[OperationStatus]
    NotOpened: _ClassVar[OperationStatus]
    Closed: _ClassVar[OperationStatus]

class StopCondition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    All: _ClassVar[StopCondition]
    Not: _ClassVar[StopCondition]
    Partial: _ClassVar[StopCondition]
    Weekday: _ClassVar[StopCondition]
    Holiday: _ClassVar[StopCondition]
    PartialStop: _ClassVar[StopCondition]

class TrainDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Both: _ClassVar[TrainDirection]
    Inbound: _ClassVar[TrainDirection]
    Outbound: _ClassVar[TrainDirection]

class TrainTypeKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Default: _ClassVar[TrainTypeKind]
    Branch: _ClassVar[TrainTypeKind]
    Rapid: _ClassVar[TrainTypeKind]
    Express: _ClassVar[TrainTypeKind]
    LimitedExpress: _ClassVar[TrainTypeKind]
    HighSpeedRapid: _ClassVar[TrainTypeKind]

class DistanceResponseState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Away: _ClassVar[DistanceResponseState]
    Arrived: _ClassVar[DistanceResponseState]
    Approaching: _ClassVar[DistanceResponseState]

class LineType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OtherLineType: _ClassVar[LineType]
    BulletTrain: _ClassVar[LineType]
    Normal: _ClassVar[LineType]
    Subway: _ClassVar[LineType]
    Tram: _ClassVar[LineType]
    MonorailOrAGT: _ClassVar[LineType]

class CompanyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OtherCompany: _ClassVar[CompanyType]
    JR: _ClassVar[CompanyType]
    Private: _ClassVar[CompanyType]
    Major: _ClassVar[CompanyType]
    SemiMajor: _ClassVar[CompanyType]
InOperation: OperationStatus
NotOpened: OperationStatus
Closed: OperationStatus
All: StopCondition
Not: StopCondition
Partial: StopCondition
Weekday: StopCondition
Holiday: StopCondition
PartialStop: StopCondition
Both: TrainDirection
Inbound: TrainDirection
Outbound: TrainDirection
Default: TrainTypeKind
Branch: TrainTypeKind
Rapid: TrainTypeKind
Express: TrainTypeKind
LimitedExpress: TrainTypeKind
HighSpeedRapid: TrainTypeKind
Away: DistanceResponseState
Arrived: DistanceResponseState
Approaching: DistanceResponseState
OtherLineType: LineType
BulletTrain: LineType
Normal: LineType
Subway: LineType
Tram: LineType
MonorailOrAGT: LineType
OtherCompany: CompanyType
JR: CompanyType
Private: CompanyType
Major: CompanyType
SemiMajor: CompanyType

class GetStationByIdRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetStationByIdListRequest(_message.Message):
    __slots__ = ("ids",)
    IDS_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, ids: _Optional[_Iterable[int]] = ...) -> None: ...

class GetStationByGroupIdRequest(_message.Message):
    __slots__ = ("group_id",)
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    def __init__(self, group_id: _Optional[int] = ...) -> None: ...

class GetStationByCoordinatesRequest(_message.Message):
    __slots__ = ("latitude", "longitude", "limit")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    limit: int
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., limit: _Optional[int] = ...) -> None: ...

class GetStationByLineIdRequest(_message.Message):
    __slots__ = ("line_id", "station_id")
    LINE_ID_FIELD_NUMBER: _ClassVar[int]
    STATION_ID_FIELD_NUMBER: _ClassVar[int]
    line_id: int
    station_id: int
    def __init__(self, line_id: _Optional[int] = ..., station_id: _Optional[int] = ...) -> None: ...

class GetStationsByNameRequest(_message.Message):
    __slots__ = ("station_name", "limit", "from_station_group_id")
    STATION_NAME_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    FROM_STATION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    station_name: str
    limit: int
    from_station_group_id: int
    def __init__(self, station_name: _Optional[str] = ..., limit: _Optional[int] = ..., from_station_group_id: _Optional[int] = ...) -> None: ...

class GetRouteRequest(_message.Message):
    __slots__ = ("from_station_group_id", "to_station_group_id", "page_size", "page_token")
    FROM_STATION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    TO_STATION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    from_station_group_id: int
    to_station_group_id: int
    page_size: int
    page_token: str
    def __init__(self, from_station_group_id: _Optional[int] = ..., to_station_group_id: _Optional[int] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class GetStationsByLineGroupIdRequest(_message.Message):
    __slots__ = ("line_group_id",)
    LINE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    line_group_id: int
    def __init__(self, line_group_id: _Optional[int] = ...) -> None: ...

class GetTrainTypesByStationIdRequest(_message.Message):
    __slots__ = ("station_id",)
    STATION_ID_FIELD_NUMBER: _ClassVar[int]
    station_id: int
    def __init__(self, station_id: _Optional[int] = ...) -> None: ...

class GetLineByIdRequest(_message.Message):
    __slots__ = ("line_id",)
    LINE_ID_FIELD_NUMBER: _ClassVar[int]
    line_id: int
    def __init__(self, line_id: _Optional[int] = ...) -> None: ...

class CoordinatesRequest(_message.Message):
    __slots__ = ("latitude", "longitude", "line_id")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    LINE_ID_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    line_id: int
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., line_id: _Optional[int] = ...) -> None: ...

class GetLinesByNameRequest(_message.Message):
    __slots__ = ("line_name", "limit")
    LINE_NAME_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    line_name: str
    limit: int
    def __init__(self, line_name: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class GetConnectedStationsRequest(_message.Message):
    __slots__ = ("from_station_group_id", "to_station_group_id")
    FROM_STATION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    TO_STATION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    from_station_group_id: int
    to_station_group_id: int
    def __init__(self, from_station_group_id: _Optional[int] = ..., to_station_group_id: _Optional[int] = ...) -> None: ...

class StationNumber(_message.Message):
    __slots__ = ("line_symbol", "line_symbol_color", "line_symbol_shape", "station_number")
    LINE_SYMBOL_FIELD_NUMBER: _ClassVar[int]
    LINE_SYMBOL_COLOR_FIELD_NUMBER: _ClassVar[int]
    LINE_SYMBOL_SHAPE_FIELD_NUMBER: _ClassVar[int]
    STATION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    line_symbol: str
    line_symbol_color: str
    line_symbol_shape: str
    station_number: str
    def __init__(self, line_symbol: _Optional[str] = ..., line_symbol_color: _Optional[str] = ..., line_symbol_shape: _Optional[str] = ..., station_number: _Optional[str] = ...) -> None: ...

class TrainType(_message.Message):
    __slots__ = ("id", "type_id", "group_id", "name", "name_katakana", "name_roman", "name_chinese", "name_korean", "color", "lines", "line", "direction", "kind")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_KATAKANA_FIELD_NUMBER: _ClassVar[int]
    NAME_ROMAN_FIELD_NUMBER: _ClassVar[int]
    NAME_CHINESE_FIELD_NUMBER: _ClassVar[int]
    NAME_KOREAN_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    LINES_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    id: int
    type_id: int
    group_id: int
    name: str
    name_katakana: str
    name_roman: str
    name_chinese: str
    name_korean: str
    color: str
    lines: _containers.RepeatedCompositeFieldContainer[Line]
    line: Line
    direction: TrainDirection
    kind: TrainTypeKind
    def __init__(self, id: _Optional[int] = ..., type_id: _Optional[int] = ..., group_id: _Optional[int] = ..., name: _Optional[str] = ..., name_katakana: _Optional[str] = ..., name_roman: _Optional[str] = ..., name_chinese: _Optional[str] = ..., name_korean: _Optional[str] = ..., color: _Optional[str] = ..., lines: _Optional[_Iterable[_Union[Line, _Mapping]]] = ..., line: _Optional[_Union[Line, _Mapping]] = ..., direction: _Optional[_Union[TrainDirection, str]] = ..., kind: _Optional[_Union[TrainTypeKind, str]] = ...) -> None: ...

class Station(_message.Message):
    __slots__ = ("id", "group_id", "name", "name_katakana", "name_roman", "name_chinese", "name_korean", "three_letter_code", "lines", "line", "prefecture_id", "postal_code", "address", "latitude", "longitude", "opened_at", "closed_at", "status", "station_numbers", "stop_condition", "distance", "has_train_types", "train_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_KATAKANA_FIELD_NUMBER: _ClassVar[int]
    NAME_ROMAN_FIELD_NUMBER: _ClassVar[int]
    NAME_CHINESE_FIELD_NUMBER: _ClassVar[int]
    NAME_KOREAN_FIELD_NUMBER: _ClassVar[int]
    THREE_LETTER_CODE_FIELD_NUMBER: _ClassVar[int]
    LINES_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    PREFECTURE_ID_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    OPENED_AT_FIELD_NUMBER: _ClassVar[int]
    CLOSED_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATION_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    STOP_CONDITION_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_FIELD_NUMBER: _ClassVar[int]
    HAS_TRAIN_TYPES_FIELD_NUMBER: _ClassVar[int]
    TRAIN_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    group_id: int
    name: str
    name_katakana: str
    name_roman: str
    name_chinese: str
    name_korean: str
    three_letter_code: str
    lines: _containers.RepeatedCompositeFieldContainer[Line]
    line: Line
    prefecture_id: int
    postal_code: str
    address: str
    latitude: float
    longitude: float
    opened_at: str
    closed_at: str
    status: OperationStatus
    station_numbers: _containers.RepeatedCompositeFieldContainer[StationNumber]
    stop_condition: StopCondition
    distance: float
    has_train_types: bool
    train_type: TrainType
    def __init__(self, id: _Optional[int] = ..., group_id: _Optional[int] = ..., name: _Optional[str] = ..., name_katakana: _Optional[str] = ..., name_roman: _Optional[str] = ..., name_chinese: _Optional[str] = ..., name_korean: _Optional[str] = ..., three_letter_code: _Optional[str] = ..., lines: _Optional[_Iterable[_Union[Line, _Mapping]]] = ..., line: _Optional[_Union[Line, _Mapping]] = ..., prefecture_id: _Optional[int] = ..., postal_code: _Optional[str] = ..., address: _Optional[str] = ..., latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., opened_at: _Optional[str] = ..., closed_at: _Optional[str] = ..., status: _Optional[_Union[OperationStatus, str]] = ..., station_numbers: _Optional[_Iterable[_Union[StationNumber, _Mapping]]] = ..., stop_condition: _Optional[_Union[StopCondition, str]] = ..., distance: _Optional[float] = ..., has_train_types: bool = ..., train_type: _Optional[_Union[TrainType, _Mapping]] = ...) -> None: ...

class SingleStationResponse(_message.Message):
    __slots__ = ("station",)
    STATION_FIELD_NUMBER: _ClassVar[int]
    station: Station
    def __init__(self, station: _Optional[_Union[Station, _Mapping]] = ...) -> None: ...

class MultipleStationResponse(_message.Message):
    __slots__ = ("stations",)
    STATIONS_FIELD_NUMBER: _ClassVar[int]
    stations: _containers.RepeatedCompositeFieldContainer[Station]
    def __init__(self, stations: _Optional[_Iterable[_Union[Station, _Mapping]]] = ...) -> None: ...

class MultipleTrainTypeResponse(_message.Message):
    __slots__ = ("train_types",)
    TRAIN_TYPES_FIELD_NUMBER: _ClassVar[int]
    train_types: _containers.RepeatedCompositeFieldContainer[TrainType]
    def __init__(self, train_types: _Optional[_Iterable[_Union[TrainType, _Mapping]]] = ...) -> None: ...

class SingleLineResponse(_message.Message):
    __slots__ = ("line",)
    LINE_FIELD_NUMBER: _ClassVar[int]
    line: Line
    def __init__(self, line: _Optional[_Union[Line, _Mapping]] = ...) -> None: ...

class MultipleLineResponse(_message.Message):
    __slots__ = ("lines",)
    LINES_FIELD_NUMBER: _ClassVar[int]
    lines: _containers.RepeatedCompositeFieldContainer[Line]
    def __init__(self, lines: _Optional[_Iterable[_Union[Line, _Mapping]]] = ...) -> None: ...

class DistanceResponse(_message.Message):
    __slots__ = ("station_id", "distance", "state")
    STATION_ID_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    station_id: int
    distance: float
    state: DistanceResponseState
    def __init__(self, station_id: _Optional[int] = ..., distance: _Optional[float] = ..., state: _Optional[_Union[DistanceResponseState, str]] = ...) -> None: ...

class RouteResponse(_message.Message):
    __slots__ = ("routes", "next_page_token")
    ROUTES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    routes: _containers.RepeatedCompositeFieldContainer[Route]
    next_page_token: str
    def __init__(self, routes: _Optional[_Iterable[_Union[Route, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class LineSymbol(_message.Message):
    __slots__ = ("symbol", "color", "shape")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    color: str
    shape: str
    def __init__(self, symbol: _Optional[str] = ..., color: _Optional[str] = ..., shape: _Optional[str] = ...) -> None: ...

class Company(_message.Message):
    __slots__ = ("id", "railroad_id", "name_short", "name_katakana", "name_full", "name_english_short", "name_english_full", "url", "type", "status", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    RAILROAD_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_SHORT_FIELD_NUMBER: _ClassVar[int]
    NAME_KATAKANA_FIELD_NUMBER: _ClassVar[int]
    NAME_FULL_FIELD_NUMBER: _ClassVar[int]
    NAME_ENGLISH_SHORT_FIELD_NUMBER: _ClassVar[int]
    NAME_ENGLISH_FULL_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    railroad_id: int
    name_short: str
    name_katakana: str
    name_full: str
    name_english_short: str
    name_english_full: str
    url: str
    type: CompanyType
    status: OperationStatus
    name: str
    def __init__(self, id: _Optional[int] = ..., railroad_id: _Optional[int] = ..., name_short: _Optional[str] = ..., name_katakana: _Optional[str] = ..., name_full: _Optional[str] = ..., name_english_short: _Optional[str] = ..., name_english_full: _Optional[str] = ..., url: _Optional[str] = ..., type: _Optional[_Union[CompanyType, str]] = ..., status: _Optional[_Union[OperationStatus, str]] = ..., name: _Optional[str] = ...) -> None: ...

class Line(_message.Message):
    __slots__ = ("id", "name_short", "name_katakana", "name_full", "name_roman", "name_chinese", "name_korean", "color", "line_type", "line_symbols", "status", "station", "company", "train_type", "average_distance")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_SHORT_FIELD_NUMBER: _ClassVar[int]
    NAME_KATAKANA_FIELD_NUMBER: _ClassVar[int]
    NAME_FULL_FIELD_NUMBER: _ClassVar[int]
    NAME_ROMAN_FIELD_NUMBER: _ClassVar[int]
    NAME_CHINESE_FIELD_NUMBER: _ClassVar[int]
    NAME_KOREAN_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    LINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LINE_SYMBOLS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATION_FIELD_NUMBER: _ClassVar[int]
    COMPANY_FIELD_NUMBER: _ClassVar[int]
    TRAIN_TYPE_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    id: int
    name_short: str
    name_katakana: str
    name_full: str
    name_roman: str
    name_chinese: str
    name_korean: str
    color: str
    line_type: LineType
    line_symbols: _containers.RepeatedCompositeFieldContainer[LineSymbol]
    status: OperationStatus
    station: Station
    company: Company
    train_type: TrainType
    average_distance: float
    def __init__(self, id: _Optional[int] = ..., name_short: _Optional[str] = ..., name_katakana: _Optional[str] = ..., name_full: _Optional[str] = ..., name_roman: _Optional[str] = ..., name_chinese: _Optional[str] = ..., name_korean: _Optional[str] = ..., color: _Optional[str] = ..., line_type: _Optional[_Union[LineType, str]] = ..., line_symbols: _Optional[_Iterable[_Union[LineSymbol, _Mapping]]] = ..., status: _Optional[_Union[OperationStatus, str]] = ..., station: _Optional[_Union[Station, _Mapping]] = ..., company: _Optional[_Union[Company, _Mapping]] = ..., train_type: _Optional[_Union[TrainType, _Mapping]] = ..., average_distance: _Optional[float] = ...) -> None: ...

class SingleLine(_message.Message):
    __slots__ = ("line",)
    LINE_FIELD_NUMBER: _ClassVar[int]
    line: Line
    def __init__(self, line: _Optional[_Union[Line, _Mapping]] = ...) -> None: ...

class MultipleLine(_message.Message):
    __slots__ = ("lines",)
    LINES_FIELD_NUMBER: _ClassVar[int]
    lines: _containers.RepeatedCompositeFieldContainer[Line]
    def __init__(self, lines: _Optional[_Iterable[_Union[Line, _Mapping]]] = ...) -> None: ...

class Route(_message.Message):
    __slots__ = ("id", "stops")
    ID_FIELD_NUMBER: _ClassVar[int]
    STOPS_FIELD_NUMBER: _ClassVar[int]
    id: int
    stops: _containers.RepeatedCompositeFieldContainer[Station]
    def __init__(self, id: _Optional[int] = ..., stops: _Optional[_Iterable[_Union[Station, _Mapping]]] = ...) -> None: ...
