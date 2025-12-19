import asyncio
from mavsdk import System

class GPSReader:
    def __init__(self):
        self.lat = None
        self.lon = None
        self.alt = None

    async def connect(self):
        self.drone = System()
        await self.drone.connect(system_address="serial:///dev/ttyACM0:57600")

        async for state in self.drone.core.connection_state():
            if state.is_connected:
                print("✅ FC Connected")
                break

        asyncio.create_task(self._gps_loop())

    async def _gps_loop(self):
        async for pos in self.drone.telemetry.position():
            self.lat = pos.latitude_deg
            self.lon = pos.longitude_deg
            self.alt = pos.absolute_altitude_m
