from typing import Any
import grpc
from mcp.server.fastmcp import FastMCP
import stationapi_pb2
import stationapi_pb2_grpc

# Initialize FastMCP server
mcp = FastMCP("station")

# Constants
SAPI_API_BASE = "https://grpc.trainlcd.app"
USER_AGENT = "mcp-app/1.0"

@mcp.tool()
async def get_closest_station(lat: float, lon: float) -> str:
    """
    Get the closest station to the given latitude and longitude.
    """
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = stationapi_pb2_grpc.StationAPIStub(channel)
        response = stub.GetStationsByCoordinates(stationapi_pb2.GetStationByCoordinatesRequest(latitude=lat, longitude=lon))
    if len(response.stations) == 0:
        return { "error": "No stations found" }

    return { "station": response.stations[0].name, "lines": [line.name_short for line in response.stations[0].lines], "address": response.stations[0].address }

@mcp.tool()
async def get_stations_by_name(station_name: str) -> str:
    """
    Get stations by name.
    """

    station_name = station_name.replace("駅", "").replace("Station", "").strip()
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = stationapi_pb2_grpc.StationAPIStub(channel)
        response = stub.GetStationsByName(stationapi_pb2.GetStationsByNameRequest(station_name=station_name))
    if len(response.stations) == 0:
        return { "error": "No stations found" }

    return {
        "stations": [{
            "station": station.name,
            "lines": [line.name_short for line in station.lines],
            "address": station.address,
            "train_type": station.train_type.name,
        } for station in response.stations]
    }

@mcp.tool()
async def get_routes_by_station_names(station_name1: str, station_name2: str) -> str:
    """
    Get routes by station name.
    """

    station_name1 = station_name1.replace("駅", "").replace("Station", "").strip()
    station_name2 = station_name2.replace("駅", "").replace("Station", "").strip()
    
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = stationapi_pb2_grpc.StationAPIStub(channel)

        stations1 = stub.GetStationsByName(stationapi_pb2.GetStationsByNameRequest(station_name=station_name1, limit=10))
        if len(stations1.stations) == 0:
            return { "error": "No stations found" }
        station1 = next((station for station in stations1.stations if station.name == station_name1), None)
        if station1 is None:
            return { "error": "Station not found" }

        stations2 = stub.GetStationsByName(stationapi_pb2.GetStationsByNameRequest(station_name=station_name2, limit=10))
        if len(stations2.stations) == 0:
            return { "error": "No stations found" }
        station2 = next((station for station in stations2.stations if station.name == station_name2), None)
        if station2 is None:
            return { "error": "Station not found" }

        response = stub.GetRoutes(stationapi_pb2.GetRouteRequest(
            from_station_group_id=station1.group_id,
            to_station_group_id=station2.group_id,
        ))
    if len(response.routes) == 0:
        return { "error": "No routes found" }
    route = response.routes[0]

    return {
        "stops": [{
            "station": station.name,
            "address": station.address,
            "train_type": station.train_type.name,
        } for station in route.stops]
    }


if __name__ == "__main__":
    mcp.run(transport='stdio')

