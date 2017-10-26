# RHVH Team Logger Package

## Installation

1. get the code

```
git clone git@10.8.176.174:yaniwang/rhvh-logger.git .
```

2. install

```
$> python setup.py install
```

## Usage

### 1. Import package inside your main file, e.g.: `main.py`

```python
from rhvh_logger import mongo_logger
```

### 2. Init class with only one param from list below

```
['auto_install', 'auto_upgrade', 'auto_vdsm', 'auto_cockpit']
```
**choose one depends on which test you run, each type will map to a collection name**

```
log = mongo_logger.RhvhLogger("auto_install").init_logger()
```

**then pass this log instance from main module to child**


### 3. log message format

```
log.info(
    'whatever message you what to save',
    extra={
        'build': 'redhat-virtualization-host-4.1-20170421.0',
        'ks': 'ati_local_01.ks',
        'start_time': '19-21-41', # HH-MM-SS
    })
```

**in extra dict, `build`, `ks`, `start_time` is required, and you can add more entry if necessary**