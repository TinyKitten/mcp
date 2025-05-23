# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: stationapi.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'stationapi.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10stationapi.proto\x12\x11\x61pp.trainlcd.grpc\"#\n\x15GetStationByIdRequest\x12\n\n\x02id\x18\x01 \x01(\r\"(\n\x19GetStationByIdListRequest\x12\x0b\n\x03ids\x18\x01 \x03(\r\".\n\x1aGetStationByGroupIdRequest\x12\x10\n\x08group_id\x18\x01 \x01(\r\"c\n\x1eGetStationByCoordinatesRequest\x12\x10\n\x08latitude\x18\x01 \x01(\x01\x12\x11\n\tlongitude\x18\x02 \x01(\x01\x12\x12\n\x05limit\x18\x03 \x01(\rH\x00\x88\x01\x01\x42\x08\n\x06_limit\"T\n\x19GetStationByLineIdRequest\x12\x0f\n\x07line_id\x18\x01 \x01(\r\x12\x17\n\nstation_id\x18\x02 \x01(\rH\x00\x88\x01\x01\x42\r\n\x0b_station_id\"\x8c\x01\n\x18GetStationsByNameRequest\x12\x14\n\x0cstation_name\x18\x01 \x01(\t\x12\x12\n\x05limit\x18\x02 \x01(\rH\x00\x88\x01\x01\x12\"\n\x15\x66rom_station_group_id\x18\x03 \x01(\rH\x01\x88\x01\x01\x42\x08\n\x06_limitB\x18\n\x16_from_station_group_id\"t\n\x0fGetRouteRequest\x12\x1d\n\x15\x66rom_station_group_id\x18\x01 \x01(\r\x12\x1b\n\x13to_station_group_id\x18\x02 \x01(\r\x12\x11\n\tpage_size\x18\x03 \x01(\r\x12\x12\n\npage_token\x18\x04 \x01(\t\"8\n\x1fGetStationsByLineGroupIdRequest\x12\x15\n\rline_group_id\x18\x01 \x01(\r\"5\n\x1fGetTrainTypesByStationIdRequest\x12\x12\n\nstation_id\x18\x01 \x01(\r\"%\n\x12GetLineByIdRequest\x12\x0f\n\x07line_id\x18\x01 \x01(\r\"[\n\x12\x43oordinatesRequest\x12\x10\n\x08latitude\x18\x01 \x01(\x01\x12\x11\n\tlongitude\x18\x02 \x01(\x01\x12\x14\n\x07line_id\x18\x03 \x01(\rH\x00\x88\x01\x01\x42\n\n\x08_line_id\"H\n\x15GetLinesByNameRequest\x12\x11\n\tline_name\x18\x01 \x01(\t\x12\x12\n\x05limit\x18\x02 \x01(\rH\x00\x88\x01\x01\x42\x08\n\x06_limit\"Y\n\x1bGetConnectedStationsRequest\x12\x1d\n\x15\x66rom_station_group_id\x18\x01 \x01(\r\x12\x1b\n\x13to_station_group_id\x18\x02 \x01(\r\"r\n\rStationNumber\x12\x13\n\x0bline_symbol\x18\x01 \x01(\t\x12\x19\n\x11line_symbol_color\x18\x02 \x01(\t\x12\x19\n\x11line_symbol_shape\x18\x03 \x01(\t\x12\x16\n\x0estation_number\x18\x04 \x01(\t\"\xaf\x03\n\tTrainType\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0f\n\x07type_id\x18\x02 \x01(\r\x12\x10\n\x08group_id\x18\x03 \x01(\r\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x15\n\rname_katakana\x18\x05 \x01(\t\x12\x17\n\nname_roman\x18\x06 \x01(\tH\x00\x88\x01\x01\x12\x19\n\x0cname_chinese\x18\x07 \x01(\tH\x01\x88\x01\x01\x12\x18\n\x0bname_korean\x18\x08 \x01(\tH\x02\x88\x01\x01\x12\r\n\x05\x63olor\x18\t \x01(\t\x12&\n\x05lines\x18\n \x03(\x0b\x32\x17.app.trainlcd.grpc.Line\x12*\n\x04line\x18\x0b \x01(\x0b\x32\x17.app.trainlcd.grpc.LineH\x03\x88\x01\x01\x12\x34\n\tdirection\x18\x0c \x01(\x0e\x32!.app.trainlcd.grpc.TrainDirection\x12.\n\x04kind\x18\r \x01(\x0e\x32 .app.trainlcd.grpc.TrainTypeKindB\r\n\x0b_name_romanB\x0f\n\r_name_chineseB\x0e\n\x0c_name_koreanB\x07\n\x05_line\"\xaa\x06\n\x07Station\x12\n\n\x02id\x18\x01 \x01(\r\x12\x10\n\x08group_id\x18\x02 \x01(\r\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x15\n\rname_katakana\x18\x04 \x01(\t\x12\x17\n\nname_roman\x18\x05 \x01(\tH\x00\x88\x01\x01\x12\x19\n\x0cname_chinese\x18\x06 \x01(\tH\x01\x88\x01\x01\x12\x18\n\x0bname_korean\x18\x07 \x01(\tH\x02\x88\x01\x01\x12\x1e\n\x11three_letter_code\x18\x08 \x01(\tH\x03\x88\x01\x01\x12&\n\x05lines\x18\t \x03(\x0b\x32\x17.app.trainlcd.grpc.Line\x12*\n\x04line\x18\n \x01(\x0b\x32\x17.app.trainlcd.grpc.LineH\x04\x88\x01\x01\x12\x15\n\rprefecture_id\x18\x0b \x01(\r\x12\x13\n\x0bpostal_code\x18\x0c \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\r \x01(\t\x12\x10\n\x08latitude\x18\x0e \x01(\x01\x12\x11\n\tlongitude\x18\x0f \x01(\x01\x12\x11\n\topened_at\x18\x10 \x01(\t\x12\x11\n\tclosed_at\x18\x11 \x01(\t\x12\x32\n\x06status\x18\x12 \x01(\x0e\x32\".app.trainlcd.grpc.OperationStatus\x12\x39\n\x0fstation_numbers\x18\x13 \x03(\x0b\x32 .app.trainlcd.grpc.StationNumber\x12\x38\n\x0estop_condition\x18\x14 \x01(\x0e\x32 .app.trainlcd.grpc.StopCondition\x12\x15\n\x08\x64istance\x18\x15 \x01(\x01H\x05\x88\x01\x01\x12\x1c\n\x0fhas_train_types\x18\x16 \x01(\x08H\x06\x88\x01\x01\x12\x35\n\ntrain_type\x18\x17 \x01(\x0b\x32\x1c.app.trainlcd.grpc.TrainTypeH\x07\x88\x01\x01\x42\r\n\x0b_name_romanB\x0f\n\r_name_chineseB\x0e\n\x0c_name_koreanB\x14\n\x12_three_letter_codeB\x07\n\x05_lineB\x0b\n\t_distanceB\x12\n\x10_has_train_typesB\r\n\x0b_train_type\"D\n\x15SingleStationResponse\x12+\n\x07station\x18\x01 \x01(\x0b\x32\x1a.app.trainlcd.grpc.Station\"G\n\x17MultipleStationResponse\x12,\n\x08stations\x18\x01 \x03(\x0b\x32\x1a.app.trainlcd.grpc.Station\"N\n\x19MultipleTrainTypeResponse\x12\x31\n\x0btrain_types\x18\x01 \x03(\x0b\x32\x1c.app.trainlcd.grpc.TrainType\";\n\x12SingleLineResponse\x12%\n\x04line\x18\x01 \x01(\x0b\x32\x17.app.trainlcd.grpc.Line\">\n\x14MultipleLineResponse\x12&\n\x05lines\x18\x01 \x03(\x0b\x32\x17.app.trainlcd.grpc.Line\"q\n\x10\x44istanceResponse\x12\x12\n\nstation_id\x18\x01 \x01(\r\x12\x10\n\x08\x64istance\x18\x02 \x01(\x01\x12\x37\n\x05state\x18\x03 \x01(\x0e\x32(.app.trainlcd.grpc.DistanceResponseState\"R\n\rRouteResponse\x12(\n\x06routes\x18\x01 \x03(\x0b\x32\x18.app.trainlcd.grpc.Route\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\":\n\nLineSymbol\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\r\n\x05\x63olor\x18\x02 \x01(\t\x12\r\n\x05shape\x18\x03 \x01(\t\"\xa9\x02\n\x07\x43ompany\x12\n\n\x02id\x18\x01 \x01(\r\x12\x13\n\x0brailroad_id\x18\x02 \x01(\r\x12\x12\n\nname_short\x18\x03 \x01(\t\x12\x15\n\rname_katakana\x18\x04 \x01(\t\x12\x11\n\tname_full\x18\x05 \x01(\t\x12\x1a\n\x12name_english_short\x18\x06 \x01(\t\x12\x19\n\x11name_english_full\x18\x07 \x01(\t\x12\x10\n\x03url\x18\x08 \x01(\tH\x00\x88\x01\x01\x12,\n\x04type\x18\t \x01(\x0e\x32\x1e.app.trainlcd.grpc.CompanyType\x12\x32\n\x06status\x18\n \x01(\x0e\x32\".app.trainlcd.grpc.OperationStatus\x12\x0c\n\x04name\x18\x0b \x01(\tB\x06\n\x04_url\"\xd2\x04\n\x04Line\x12\n\n\x02id\x18\x01 \x01(\r\x12\x12\n\nname_short\x18\x02 \x01(\t\x12\x15\n\rname_katakana\x18\x03 \x01(\t\x12\x11\n\tname_full\x18\x04 \x01(\t\x12\x17\n\nname_roman\x18\x05 \x01(\tH\x00\x88\x01\x01\x12\x19\n\x0cname_chinese\x18\x06 \x01(\tH\x01\x88\x01\x01\x12\x18\n\x0bname_korean\x18\x07 \x01(\tH\x02\x88\x01\x01\x12\r\n\x05\x63olor\x18\x08 \x01(\t\x12.\n\tline_type\x18\t \x01(\x0e\x32\x1b.app.trainlcd.grpc.LineType\x12\x33\n\x0cline_symbols\x18\n \x03(\x0b\x32\x1d.app.trainlcd.grpc.LineSymbol\x12\x32\n\x06status\x18\x0b \x01(\x0e\x32\".app.trainlcd.grpc.OperationStatus\x12\x30\n\x07station\x18\x0c \x01(\x0b\x32\x1a.app.trainlcd.grpc.StationH\x03\x88\x01\x01\x12\x30\n\x07\x63ompany\x18\r \x01(\x0b\x32\x1a.app.trainlcd.grpc.CompanyH\x04\x88\x01\x01\x12\x35\n\ntrain_type\x18\x0e \x01(\x0b\x32\x1c.app.trainlcd.grpc.TrainTypeH\x05\x88\x01\x01\x12\x18\n\x10\x61verage_distance\x18\x0f \x01(\x01\x42\r\n\x0b_name_romanB\x0f\n\r_name_chineseB\x0e\n\x0c_name_koreanB\n\n\x08_stationB\n\n\x08_companyB\r\n\x0b_train_type\"3\n\nSingleLine\x12%\n\x04line\x18\x01 \x01(\x0b\x32\x17.app.trainlcd.grpc.Line\"6\n\x0cMultipleLine\x12&\n\x05lines\x18\x01 \x03(\x0b\x32\x17.app.trainlcd.grpc.Line\">\n\x05Route\x12\n\n\x02id\x18\x01 \x01(\r\x12)\n\x05stops\x18\x02 \x03(\x0b\x32\x1a.app.trainlcd.grpc.Station*=\n\x0fOperationStatus\x12\x0f\n\x0bInOperation\x10\x00\x12\r\n\tNotOpened\x10\x01\x12\n\n\x06\x43losed\x10\x02*Y\n\rStopCondition\x12\x07\n\x03\x41ll\x10\x00\x12\x07\n\x03Not\x10\x01\x12\x0b\n\x07Partial\x10\x02\x12\x0b\n\x07Weekday\x10\x03\x12\x0b\n\x07Holiday\x10\x04\x12\x0f\n\x0bPartialStop\x10\x05*5\n\x0eTrainDirection\x12\x08\n\x04\x42oth\x10\x00\x12\x0b\n\x07Inbound\x10\x01\x12\x0c\n\x08Outbound\x10\x02*h\n\rTrainTypeKind\x12\x0b\n\x07\x44\x65\x66\x61ult\x10\x00\x12\n\n\x06\x42ranch\x10\x01\x12\t\n\x05Rapid\x10\x02\x12\x0b\n\x07\x45xpress\x10\x03\x12\x12\n\x0eLimitedExpress\x10\x04\x12\x12\n\x0eHighSpeedRapid\x10\x05*?\n\x15\x44istanceResponseState\x12\x08\n\x04\x41way\x10\x00\x12\x0b\n\x07\x41rrived\x10\x01\x12\x0f\n\x0b\x41pproaching\x10\x02*c\n\x08LineType\x12\x11\n\rOtherLineType\x10\x00\x12\x0f\n\x0b\x42ulletTrain\x10\x01\x12\n\n\x06Normal\x10\x02\x12\n\n\x06Subway\x10\x03\x12\x08\n\x04Tram\x10\x04\x12\x11\n\rMonorailOrAGT\x10\x05*N\n\x0b\x43ompanyType\x12\x10\n\x0cOtherCompany\x10\x00\x12\x06\n\x02JR\x10\x01\x12\x0b\n\x07Private\x10\x02\x12\t\n\x05Major\x10\x03\x12\r\n\tSemiMajor\x10\x04\x32\xbe\n\n\nStationAPI\x12\x66\n\x0eGetStationById\x12(.app.trainlcd.grpc.GetStationByIdRequest\x1a(.app.trainlcd.grpc.SingleStationResponse\"\x00\x12p\n\x12GetStationByIdList\x12,.app.trainlcd.grpc.GetStationByIdListRequest\x1a*.app.trainlcd.grpc.MultipleStationResponse\"\x00\x12s\n\x14GetStationsByGroupId\x12-.app.trainlcd.grpc.GetStationByGroupIdRequest\x1a*.app.trainlcd.grpc.MultipleStationResponse\"\x00\x12{\n\x18GetStationsByCoordinates\x12\x31.app.trainlcd.grpc.GetStationByCoordinatesRequest\x1a*.app.trainlcd.grpc.MultipleStationResponse\"\x00\x12q\n\x13GetStationsByLineId\x12,.app.trainlcd.grpc.GetStationByLineIdRequest\x1a*.app.trainlcd.grpc.MultipleStationResponse\"\x00\x12n\n\x11GetStationsByName\x12+.app.trainlcd.grpc.GetStationsByNameRequest\x1a*.app.trainlcd.grpc.MultipleStationResponse\"\x00\x12|\n\x18GetStationsByLineGroupId\x12\x32.app.trainlcd.grpc.GetStationsByLineGroupIdRequest\x1a*.app.trainlcd.grpc.MultipleStationResponse\"\x00\x12~\n\x18GetTrainTypesByStationId\x12\x32.app.trainlcd.grpc.GetTrainTypesByStationIdRequest\x1a,.app.trainlcd.grpc.MultipleTrainTypeResponse\"\x00\x12S\n\tGetRoutes\x12\".app.trainlcd.grpc.GetRouteRequest\x1a .app.trainlcd.grpc.RouteResponse\"\x00\x12]\n\x0bGetLineById\x12%.app.trainlcd.grpc.GetLineByIdRequest\x1a%.app.trainlcd.grpc.SingleLineResponse\"\x00\x12\x65\n\x0eGetLinesByName\x12(.app.trainlcd.grpc.GetLinesByNameRequest\x1a\'.app.trainlcd.grpc.MultipleLineResponse\"\x00\x12h\n\x12GetConnectedRoutes\x12..app.trainlcd.grpc.GetConnectedStationsRequest\x1a .app.trainlcd.grpc.RouteResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'stationapi_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_OPERATIONSTATUS']._serialized_start=4064
  _globals['_OPERATIONSTATUS']._serialized_end=4125
  _globals['_STOPCONDITION']._serialized_start=4127
  _globals['_STOPCONDITION']._serialized_end=4216
  _globals['_TRAINDIRECTION']._serialized_start=4218
  _globals['_TRAINDIRECTION']._serialized_end=4271
  _globals['_TRAINTYPEKIND']._serialized_start=4273
  _globals['_TRAINTYPEKIND']._serialized_end=4377
  _globals['_DISTANCERESPONSESTATE']._serialized_start=4379
  _globals['_DISTANCERESPONSESTATE']._serialized_end=4442
  _globals['_LINETYPE']._serialized_start=4444
  _globals['_LINETYPE']._serialized_end=4543
  _globals['_COMPANYTYPE']._serialized_start=4545
  _globals['_COMPANYTYPE']._serialized_end=4623
  _globals['_GETSTATIONBYIDREQUEST']._serialized_start=39
  _globals['_GETSTATIONBYIDREQUEST']._serialized_end=74
  _globals['_GETSTATIONBYIDLISTREQUEST']._serialized_start=76
  _globals['_GETSTATIONBYIDLISTREQUEST']._serialized_end=116
  _globals['_GETSTATIONBYGROUPIDREQUEST']._serialized_start=118
  _globals['_GETSTATIONBYGROUPIDREQUEST']._serialized_end=164
  _globals['_GETSTATIONBYCOORDINATESREQUEST']._serialized_start=166
  _globals['_GETSTATIONBYCOORDINATESREQUEST']._serialized_end=265
  _globals['_GETSTATIONBYLINEIDREQUEST']._serialized_start=267
  _globals['_GETSTATIONBYLINEIDREQUEST']._serialized_end=351
  _globals['_GETSTATIONSBYNAMEREQUEST']._serialized_start=354
  _globals['_GETSTATIONSBYNAMEREQUEST']._serialized_end=494
  _globals['_GETROUTEREQUEST']._serialized_start=496
  _globals['_GETROUTEREQUEST']._serialized_end=612
  _globals['_GETSTATIONSBYLINEGROUPIDREQUEST']._serialized_start=614
  _globals['_GETSTATIONSBYLINEGROUPIDREQUEST']._serialized_end=670
  _globals['_GETTRAINTYPESBYSTATIONIDREQUEST']._serialized_start=672
  _globals['_GETTRAINTYPESBYSTATIONIDREQUEST']._serialized_end=725
  _globals['_GETLINEBYIDREQUEST']._serialized_start=727
  _globals['_GETLINEBYIDREQUEST']._serialized_end=764
  _globals['_COORDINATESREQUEST']._serialized_start=766
  _globals['_COORDINATESREQUEST']._serialized_end=857
  _globals['_GETLINESBYNAMEREQUEST']._serialized_start=859
  _globals['_GETLINESBYNAMEREQUEST']._serialized_end=931
  _globals['_GETCONNECTEDSTATIONSREQUEST']._serialized_start=933
  _globals['_GETCONNECTEDSTATIONSREQUEST']._serialized_end=1022
  _globals['_STATIONNUMBER']._serialized_start=1024
  _globals['_STATIONNUMBER']._serialized_end=1138
  _globals['_TRAINTYPE']._serialized_start=1141
  _globals['_TRAINTYPE']._serialized_end=1572
  _globals['_STATION']._serialized_start=1575
  _globals['_STATION']._serialized_end=2385
  _globals['_SINGLESTATIONRESPONSE']._serialized_start=2387
  _globals['_SINGLESTATIONRESPONSE']._serialized_end=2455
  _globals['_MULTIPLESTATIONRESPONSE']._serialized_start=2457
  _globals['_MULTIPLESTATIONRESPONSE']._serialized_end=2528
  _globals['_MULTIPLETRAINTYPERESPONSE']._serialized_start=2530
  _globals['_MULTIPLETRAINTYPERESPONSE']._serialized_end=2608
  _globals['_SINGLELINERESPONSE']._serialized_start=2610
  _globals['_SINGLELINERESPONSE']._serialized_end=2669
  _globals['_MULTIPLELINERESPONSE']._serialized_start=2671
  _globals['_MULTIPLELINERESPONSE']._serialized_end=2733
  _globals['_DISTANCERESPONSE']._serialized_start=2735
  _globals['_DISTANCERESPONSE']._serialized_end=2848
  _globals['_ROUTERESPONSE']._serialized_start=2850
  _globals['_ROUTERESPONSE']._serialized_end=2932
  _globals['_LINESYMBOL']._serialized_start=2934
  _globals['_LINESYMBOL']._serialized_end=2992
  _globals['_COMPANY']._serialized_start=2995
  _globals['_COMPANY']._serialized_end=3292
  _globals['_LINE']._serialized_start=3295
  _globals['_LINE']._serialized_end=3889
  _globals['_SINGLELINE']._serialized_start=3891
  _globals['_SINGLELINE']._serialized_end=3942
  _globals['_MULTIPLELINE']._serialized_start=3944
  _globals['_MULTIPLELINE']._serialized_end=3998
  _globals['_ROUTE']._serialized_start=4000
  _globals['_ROUTE']._serialized_end=4062
  _globals['_STATIONAPI']._serialized_start=4626
  _globals['_STATIONAPI']._serialized_end=5968
# @@protoc_insertion_point(module_scope)
