import sys
sys.path.append(".")
from loguru import logging
class Staff:
    def __init__(self,name,id,account,password,permission) -> None:
        self.name = name
        self.id = id
        self.account = account
        # self.password = password include in account
        self._get_permission(permission=permission)
    def _get_permission(self,permission):
        self.permissions = ["managers","employee"]
        if self.permission not in self.permissions:
            logging.info("Can not create new employees")
            pass
        else:
            self.permission = permission    