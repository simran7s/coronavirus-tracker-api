"""app.data"""
from app.services.location.locationServiceAdapter import Adapter
from ..services.location.csbs import CSBSLocationService
from ..services.location.jhu import JhuLocationService
from ..services.location.nyt import NYTLocationService

# Mapping of services to data-sources.
DATA_SOURCES = {
    "jhu": JhuLocationService(),
    "csbs": CSBSLocationService(),
    "nyt": NYTLocationService(),
}


def data_source(source):
    """
    Retrieves the provided data-source service.

    :returns: The service.
    :rtype: LocationService
    """

    return Adapter(DATA_SOURCES.get(source.lower()))
