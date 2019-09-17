# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _


def get_data():
    return [
        {
            "label": _("Settings"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Wire Transfer Settings",
                    "description": _("Wire Transfer Settings"),
                }
            ],
        },
    ]
