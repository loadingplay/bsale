#!/usr/bin/python
# -*- coding: UTF-8 -*-

from .constants import Endpoints
from .endpoint import Endpoint


class Offices(Endpoint):

    def getOne(
        self,
        office_id
    ):
        return self.get(
            Endpoints.OFFICES_ID.format(office_id)
        )
