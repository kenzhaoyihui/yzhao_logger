from rhvh_logger import mongo_logger

log = mongo_logger.RhvhLogger("auto_vdsm").init_logger()

log.info("Test VDSM!")