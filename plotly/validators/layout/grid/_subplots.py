#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class SubplotsValidator(_bv.InfoArrayValidator):
    def __init__(self, plotly_name="subplots", parent_name="layout.grid", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            dimensions=kwargs.pop("dimensions", 2),
            edit_type=kwargs.pop("edit_type", "plot"),
            free_length=kwargs.pop("free_length", True),
            items=kwargs.pop(
                "items",
                {
                    "editType": "plot",
                    "valType": "enumerated",
                    "values": ["/^x([2-9]|[1-9][0-9]+)?y([2-9]|[1-9][0-9]+)?$/", ""],
                },
            ),
            **kwargs,
        )
