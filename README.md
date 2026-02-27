# ArcGIS API for Python - Automated Testing Framework 🗺️

![Test Status](https://github.com/juan-palomares/arcgis-api-testing-framework/actions/workflows/test-arcgis.yml/badge.svg)
![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue)
![ArcGIS API](https://img.shields.io/badge/ArcGIS%20API-2.1%2B-green)

Comprehensive automated testing framework for the **ArcGIS API for Python** with CI/CD integration via GitHub Actions.

## 🎯 Purpose

This project demonstrates:
- Automated testing workflows for geospatial APIs
- CI/CD integration for Python packages
- Quality assurance practices for API releases
- Multi-version Python compatibility testing

Built to showcase DevOps skills applicable to supporting the ArcGIS API for Python development and release pipeline.

## ✨ Features

### Core Functionality Tests
- ✅ GIS connection and authentication
- ✅ Geocoding and reverse geocoding
- ✅ Content search and discovery
- ✅ Geometry operations
- ✅ API version verification

### Feature Service Tests
- ✅ Feature layer queries
- ✅ SQL where clause filtering
- ✅ Spatial queries and extent
- ✅ Feature counting and metadata
- ✅ Schema and field inspection

### CI/CD Automation
- ✅ Automated tests on every push
- ✅ Multi-version Python testing (3.9, 3.10, 3.11)
- ✅ Daily scheduled test runs
- ✅ Manual workflow triggering
- ✅ Test summary reporting

## 🛠️ Technologies

- **ArcGIS API for Python 2.1+**
- **Python 3.9, 3.10, 3.11**
- **unittest** framework
- **GitHub Actions** for CI/CD
- **Esri ArcGIS Online** public services

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/juan-palomares/arcgis-api-testing-framework.git
cd arcgis-api-testing-framework

# Install dependencies
pip install -r requirements.txt

# Verify installation
python -c "import arcgis; print(f'✅ ArcGIS API version: {arcgis.__version__}')"
```
🧪 Running Tests
Run All Tests
```
Bash

python -m unittest discover -v

Run Specific Test Suites
```
```
Bash

# Core API tests
python -m unittest test_arcgis_core.py -v

# Feature layer tests
python -m unittest test_arcgis_features.py -v

Run Individual Test Classes
```
```
Bash

python -m unittest test_arcgis_core.TestGeocoding -v
```
## 📊 Test Coverage
Test Suite	Tests	Coverage
Core API	12 tests	Connection, Geocoding, Search, Geometry
Feature Services	6 tests	Queries, Filtering, Metadata
Total	18 tests	Comprehensive API validation
🔄 CI/CD Pipeline
Automated Workflows

On Every Push:

    Runs full test suite across Python 3.9, 3.10, 3.11
    Validates API compatibility
    Reports test results

Daily Schedule (9 AM UTC):

    Automated regression testing
    Ensures API endpoint availability
    Monitors for breaking changes

Manual Trigger:

    On-demand test execution via GitHub Actions UI

Workflow Configuration
```
YAML

# Runs on: push, pull_request, schedule, workflow_dispatch
strategy:
  matrix:
    python-version: ["3.9", "3.10", "3.11"]
```
📝 Sample Test Output
```
text

test_arcgis_version (test_arcgis_core.TestAPIVersion.test_arcgis_version)
Test that ArcGIS version is available. ... ok
test_required_modules_available (test_arcgis_core.TestAPIVersion.test_required_modules_available)
Test that required modules can be imported. ... ok
test_connection_established (test_arcgis_core.TestArcGISConnection.test_connection_established)
Test that connection to ArcGIS Online is successful. ... ok
Test that GIS object has expected properties. ... ok
test_search_by_tag (test_arcgis_core.TestContentSearch.test_search_by_tag)
Test searching content by tags. ... ok
test_search_esri_content (test_arcgis_core.TestContentSearch.test_search_esri_content)
Test searching for Esri's public content. ... ok
test_search_web_maps (test_arcgis_core.TestContentSearch.test_search_web_maps)
Test searching for web maps. ... ok
test_geocode_esri_headquarters (test_arcgis_core.TestGeocoding.test_geocode_esri_headquarters)
Test geocoding Esri's Redlands headquarters. ... ok
test_geocode_multiple_addresses (test_arcgis_core.TestGeocoding.test_geocode_multiple_addresses)
Test geocoding multiple addresses. ... ok
test_reverse_geocode (test_arcgis_core.TestGeocoding.test_reverse_geocode)
Test reverse geocoding (coordinates to address). ... ok
test_create_point (test_arcgis_core.TestGeometry.test_create_point)
Test creating a Point geometry. ... ok
test_point_properties (test_arcgis_core.TestGeometry.test_point_properties)
Test Point object has expected properties. ... ok
test_layer_url_accessible (test_arcgis_features.TestFeatureLayerMetadata.test_layer_url_accessible)
Test that the layer URL is accessible. ... ok
test_count_features (test_arcgis_features.TestFeatureServices.test_count_features)
Test counting features in a layer. ... ok
test_feature_layer_creation (test_arcgis_features.TestFeatureServices.test_feature_layer_creation)
Test that feature layer was created successfully. ... ok
test_query_features (test_arcgis_features.TestFeatureServices.test_query_features)
Test querying features from a layer. ... ok
test_query_multiple_records (test_arcgis_features.TestFeatureServices.test_query_multiple_records)
Test querying varying record counts. ... ok
test_query_with_geometry (test_arcgis_features.TestFeatureServices.test_query_with_geometry)
Test that query results include geometry. ... ok
test_query_with_where_clause (test_arcgis_features.TestFeatureServices.test_query_with_where_clause)
Test querying features with SQL where clause. ... ok

----------------------------------------------------------------------
Ran 19 tests in 6.196s

OK
```

## 🗺️ APIs Tested
Public Endpoints

    ArcGIS Online - Anonymous connection
    Geocoding Service - Address/coordinate conversion
    Feature Services - USA States (sample data)
    Content Search - Public items and web maps

Tested Operations

    Geocoding (forward & reverse)
    Feature queries (SQL & spatial)
    Content discovery
    Geometry creation
    Metadata access

## 📚 What I Learned
ArcGIS API Concepts

    GIS object lifecycle and connection management
    Geocoding workflows and accuracy scoring
    Feature layer querying and filtering
    Spatial reference systems
    Public vs authenticated access patterns

DevOps Skills

    Automated API testing strategies
    Multi-version compatibility validation
    CI/CD pipeline configuration
    Test isolation and mocking
    Regression testing automation
    Daily monitoring workflows

Python Best Practices

    unittest framework organization
    Class-based test structure
    setUp/tearDown patterns
    Assertions and validation
    Error handling in tests

## 🎯 DevOps Skills Demonstrated

✅ API Testing - Comprehensive endpoint validation
✅ CI/CD Automation - GitHub Actions workflows
✅ Multi-Version Testing - Python 3.9, 3.10, 3.11 compatibility
✅ Scheduled Monitoring - Daily regression tests
✅ Quality Assurance - Automated validation on every commit
✅ Documentation - Clear test organization and reporting
🚀 Future Enhancements

    Add authenticated testing (with secure credential management)
    Implement code coverage reporting
    Add performance benchmarking tests
    Test offline capabilities
    Add spatial analysis operations tests
    Integrate with ArcGIS Enterprise endpoints

🔗 Related Projects

    python-calculator-cicd - Basic CI/CD concepts
    api-health-checker - Scheduled API monitoring

📧 Contact

Juan Palomares
GitHub: @juan-palomares
