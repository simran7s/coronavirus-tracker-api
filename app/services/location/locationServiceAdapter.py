from services.location import LocationService

"""
Implement Adapter method for LocationService
"""


class Adapter (LocationService):
    # def __init__(self):
    #     self.locations

    # async def get_locations(self):
    #     self.locations = await LocationService.get_locations()

    async def get_all(self):
        # Get the locations.
        locations = await LocationService.get_locations()
        return locations

    async def get(self, loc_id):  # pylint: disable=arguments-differ
        # Get location at the index equal to the provided id.
        locations = await LocationService.get_locations()
        return locations[loc_id]
