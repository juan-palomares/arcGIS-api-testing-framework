"""
ArcGIS API for Python - Core Functionality Tests
Automated testing framework for GIS operations, geocoding, and content search.

Author: Juan Palomares
GitHub: github.com/juan-palomares
"""

import unittest
import warnings
import arcgis
from arcgis.gis import GIS
from arcgis.geocoding import geocode, reverse_geocode
from arcgis.geometry import Point


# Suppress Pydantic deprecation warnings from ArcGIS library
warnings.filterwarnings("ignore", category=DeprecationWarning)


class TestArcGISConnection(unittest.TestCase):
    """Test basic connection to ArcGIS Online."""
    
    @classmethod
    def setUpClass(cls):
        """Set up anonymous connection to ArcGIS Online."""
        cls.gis = GIS()
    
    def test_connection_established(self):
        """Test that connection to ArcGIS Online is successful."""
        self.assertIsNotNone(self.gis)
        self.assertEqual(self.gis.url, 'https://www.arcgis.com')
    
    def test_gis_properties(self):
        """Test that GIS object has expected properties."""
        self.assertTrue(hasattr(self.gis, 'content'))
        self.assertTrue(hasattr(self.gis, 'users'))
        self.assertTrue(hasattr(self.gis, 'groups'))


class TestGeocoding(unittest.TestCase):
    """Test geocoding and reverse geocoding functionality."""
    
    @classmethod
    def setUpClass(cls):
        """Set up GIS connection for geocoding."""
        cls.gis = GIS()
        arcgis.env.active_gis = cls.gis
    
    def test_geocode_esri_headquarters(self):
        """Test geocoding Esri's Redlands headquarters."""
        address = "380 New York St, Redlands, CA 92373"
        results = geocode(address, max_locations=1)
        
        self.assertGreater(len(results), 0)
        
        result = results[0]
        self.assertIn('address', result)
        self.assertIn('location', result)
        
        location = result['location']
        self.assertAlmostEqual(location['x'], -117.195, delta=0.1)
        self.assertAlmostEqual(location['y'], 34.056, delta=0.1)
    
    def test_geocode_multiple_addresses(self):
        """Test geocoding multiple addresses."""
        addresses = ["Redlands, CA", "San Diego, CA", "Los Angeles, CA"]
        
        for address in addresses:
            results = geocode(address, max_locations=1)
            self.assertGreater(len(results), 0, f"Should geocode {address}")
    
    def test_reverse_geocode(self):
        """Test reverse geocoding (coordinates to address)."""
        point = Point({"x": -117.1956, "y": 34.0560, "spatialReference": {"wkid": 4326}})
        result = reverse_geocode(point)
        
        self.assertIsNotNone(result)
        self.assertIn('address', result)
        self.assertGreater(len(result['address']['Match_addr']), 0)


class TestContentSearch(unittest.TestCase):
    """Test searching for public content on ArcGIS Online."""
    
    @classmethod
    def setUpClass(cls):
        """Set up GIS connection."""
        cls.gis = GIS()
    
    def test_search_esri_content(self):
        """Test searching for Esri's public content."""
        search_results = self.gis.content.search(
            query="owner:esri",
            item_type="Feature Service",
            max_items=5
        )
        
        self.assertGreater(len(search_results), 0)
        for item in search_results:
            self.assertIsNotNone(item.title)
    
    def test_search_by_tag(self):
        """Test searching content by tags."""
        search_results = self.gis.content.search(query="tags:basemap", max_items=3)
        self.assertGreater(len(search_results), 0)
    
    def test_search_web_maps(self):
        """Test searching for web maps."""
        search_results = self.gis.content.search(query="", item_type="Web Map", max_items=3)
        self.assertGreater(len(search_results), 0)


class TestGeometry(unittest.TestCase):
    """Test geometry operations."""
    
    def test_create_point(self):
        """Test creating a Point geometry."""
        point = Point({"x": -118.2437, "y": 34.0522, "spatialReference": {"wkid": 4326}})
        
        self.assertEqual(point.x, -118.2437)
        self.assertEqual(point.y, 34.0522)
    
    def test_point_properties(self):
        """Test Point object has expected properties."""
        point = Point({"x": -117.1956, "y": 34.0560})
        
        self.assertTrue(hasattr(point, 'x'))
        self.assertTrue(hasattr(point, 'y'))


class TestAPIVersion(unittest.TestCase):
    """Test API version and environment information."""
    
    def test_arcgis_version(self):
        """Test that ArcGIS version is available."""
        self.assertTrue(hasattr(arcgis, '__version__'))
    
    def test_required_modules_available(self):
        """Test that required modules can be imported."""
        modules = [
            'arcgis.gis',
            'arcgis.geocoding',
            'arcgis.geometry',
            'arcgis.features'
        ]
        
        for module_name in modules:
            try:
                __import__(module_name)
            except ImportError:
                self.fail(f"Required module not available: {module_name}")


if __name__ == '__main__':
    unittest.main(verbosity=2)