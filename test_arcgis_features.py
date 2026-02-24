"""
ArcGIS API for Python - Feature Layer Tests
Tests working with feature services and spatial queries.

Author: Juan Palomares
GitHub: github.com/juan-palomares
"""

import unittest
import warnings
from arcgis.gis import GIS
from arcgis.features import FeatureLayer


# Suppress deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


class TestFeatureServices(unittest.TestCase):
    """Test working with public feature services."""
    
    @classmethod
    def setUpClass(cls):
        """Set up GIS connection and test feature layer."""
        cls.gis = GIS()
        cls.countries_url = "https://services.arcgis.com/P3ePLMYs2RVChkJx/arcgis/rest/services/World_Countries_(Generalized)/FeatureServer/0"
        cls.countries_layer = FeatureLayer(cls.countries_url, gis=cls.gis)
    
    def test_feature_layer_creation(self):
        """Test that feature layer was created successfully."""
        self.assertIsNotNone(self.countries_layer)
        self.assertTrue(hasattr(self.countries_layer, 'query'))
    
    def test_query_features(self):
        """Test querying features from a layer."""
        feature_set = self.countries_layer.query(
            where="1=1", 
            return_count_only=False, 
            result_record_count=5
        )
        
        self.assertIsNotNone(feature_set)
        self.assertTrue(hasattr(feature_set, 'features'))
        self.assertGreater(len(feature_set.features), 0)
    
    def test_query_with_where_clause(self):
        """Test querying features with SQL where clause."""
        feature_set = self.countries_layer.query(where="1=1", result_record_count=3)
        self.assertGreater(len(feature_set.features), 0)
    
    def test_count_features(self):
        """Test counting features in a layer."""
        count = self.countries_layer.query(where="1=1", return_count_only=True)
        self.assertGreater(count, 100)
    
    def test_query_with_geometry(self):
        """Test that query results include geometry."""
        feature_set = self.countries_layer.query(
            where="1=1", 
            return_geometry=True,
            result_record_count=1
        )
        
        self.assertGreater(len(feature_set.features), 0)
        self.assertTrue(hasattr(feature_set.features[0], 'geometry'))
    
    def test_query_multiple_records(self):
        """Test querying varying record counts."""
        for count in [5, 10, 20]:
            feature_set = self.countries_layer.query(where="1=1", result_record_count=count)
            self.assertGreater(len(feature_set.features), 0)
            self.assertLessEqual(len(feature_set.features), count)


class TestFeatureLayerMetadata(unittest.TestCase):
    """Test accessing feature layer metadata."""
    
    def test_layer_url_accessible(self):
        """Test that the layer URL is accessible."""
        gis = GIS()
        countries_url = "https://services.arcgis.com/P3ePLMYs2RVChkJx/arcgis/rest/services/World_Countries_(Generalized)/FeatureServer/0"
        layer = FeatureLayer(countries_url, gis=gis)
        
        self.assertIsNotNone(layer)
        self.assertEqual(layer.url, countries_url)


if __name__ == '__main__':
    unittest.main(verbosity=2)