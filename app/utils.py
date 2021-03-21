"""

"""
from datetime import date, datetime
from decimal import Decimal
import flask


class MyJSONEncoder(flask.json.JSONEncoder):
    """JSON serializer for objects not serializable by default json code"""
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        if isinstance(obj, Decimal):
            return float(obj)
        # if isinstance(obj, Decimal):
        #     return str(obj)
        return super(MyJSONEncoder, self).default(obj)


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError("Type %s not serializable" % type(obj))
