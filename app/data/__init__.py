"""app.data"""
from ..services.location.csbs import CSBSLocationService
from ..services.location.jhu import JhuLocationService
from ..services.location.nyt import NYTLocationService


class DataSourceSingleton:
    # variable storing the ONLY (if any) DataSourceSingle instance
    _instance = None

    def __new__(self):
        """
        Creates new DataSourceSingleton instance iff one does not exist.
        Otherwise, existing instance is used.
        Then returns the new/existing instance.

        :returns: new/existing instance of DataSourceSingleton object.
        :rtype: DataSourceSingleton
        """

        if not DataSourceSingleton._instance:
            DataSourceSingleton._instance = super(
                DataSourceSingleton, self).__new__(self)

            # Mapping of services to data-sources.
            self._DATA_SOURCES = {
                "jhu": JhuLocationService(),
                "csbs": CSBSLocationService(),
                "nyt": NYTLocationService(),
            }
        return DataSourceSingleton._instance


def data_source(source):
    """
    Retrieves the provided data-source service.

    :returns: The service.
    :rtype: LocationService
    """
    storedSources = DataSourceSingleton()
    return storedSources._DATA_SOURCES.get(source.lower())
