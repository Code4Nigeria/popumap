# pull in the default wazimap settings
from wazimap.settings import *  # noqa

# install this app before Wazimap
INSTALLED_APPS = ['popumap_1'] + INSTALLED_APPS

# Localise this instance of Wazimap
WAZIMAP['name'] = 'PopuMap Nigeria Census data'
# NB: this must be https if your site supports HTTPS.
WAZIMAP['url'] = 'http://localhost:8000'
WAZIMAP['country_code'] = 'NG'
WAZIMAP['geometry_data'] = {'country': 'geo/country.topojson',
                            'state': 'geo/state.topojson',
                            'lga': 'geo/lga.topojson'}
WAZIMAP['profile_builder'] = 'popumap_1.profiles.get_census_profile'
WAZIMAP['levels'] = {
    'country':{
    'name':'country',
    'plural': 'countries',
    'children':['state']
            },
    'state' :{
    'name' :'state',
    'plural': 'states',
    'children':['lga']
    },
    'lga' :{
    'name' : 'lga',
    'plural':'lgas',
    'children':['ward']
    },
    'ward':{
    'name' : 'ward',
    'plural' :'wards',
    'children' :['pu']
    },
    'pu':{
    'name' : 'pu',
    'plural' :'pus',
    }
    }