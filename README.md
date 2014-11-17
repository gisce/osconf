osconf
======

Configure from environment variables


```python

from osconf import config_from_environment

class Service(object):
    def __init__(self, param1, param2=None, param3=None):
      self.param1 = param2
      self.param2 = param2
      self.param3 = param3
  
config = config_from_environment('SERVICE', ['param1'])

# Environ variables must be defined with 'SERVICE' prefix and the key
# export SERVICE_PARAM1='Hi'

service = Service(**config)

# You can pass default values to config_from_environment

default_config = {
  'param1': 'Foo',
  'param2': 'Bar',
  'param3': 'Niu'
}

config = config_from_environment('SERVICE', ['param1'], **default_config)

# If some is defined in environment, the environment is taken

service = Service(**config)

```
