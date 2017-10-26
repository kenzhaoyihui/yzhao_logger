import logging
import attr
from log4mongo.handlers import MongoHandler

_TEST_TYPES = ('auto_install', 'auto_upgrade', 'auto_vdsm', 'auto_cockpit')


@attr.s
class RhvhLogger(object):
    test_type = attr.ib()

    @test_type.validator
    def check(self, attribute, value):
        if value not in _TEST_TYPES:
            raise ValueError('value must be one of %s' % _TEST_TYPES)

    log_level = attr.ib(default=logging.INFO)

    mongo_host = attr.ib(default='10.66.8.111')
    mongo_db = attr.ib(default='rhvh_logs')
    mongo_auth_db = attr.ib(default='rhvh_logs')
    mongo_user = attr.ib(default='rhvhlogger')
    mongo_pass = attr.ib(default='rhvhlogger')

    def init_logger(self):
        print self.log_level
        logger = logging.getLogger(self.test_type)
        logger.addHandler(
            MongoHandler(
                host=self.mongo_host,
                database_name=self.mongo_db,
                authentication_db=self.mongo_auth_db,
                username=self.mongo_user,
                password=self.mongo_pass,
                collection=self.test_type))
        logger.setLevel(self.log_level)
        return logger
