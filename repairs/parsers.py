import csv
import re
from datetime import datetime, timezone

from django.contrib.gis.geos import Point

from repairs.models.constants import QuickDescription, SpecialCase


class MeasurementParser:
    """Measurement record parser for CSV file"""

    _columns = {
        "OBJECTID": "object_id",
        "H1": "h1",
        "H2": "h2",
        "Survey Address": "survey_address",
        # "City": "city",
        # "State": "state",
        # "Country": "country",
        # "Zip Code": "zip_code",
        "Special Case": "special_case",
        "Quick Description": "quick_description",
        # "Lineal Feet": "lineal_feet",
        # "Inch Feet": "inch_feet",
        # "Cost": "cost",
        "Notes": "note",
        "Length": "length",
        "Width": "width",
        # "Quality": "quality",
        "CreationDate": "measured_at",
    }

    def parse(self, file_obj):
        """Parse the CSV file into a list of records"""
        file_obj.seek(0)
        records = []

        for data in csv.DictReader(file_obj, delimiter=","):
            item = {}

            # Parse the simple fields
            for key, alias in self._columns.items():
                value = str(data.get(key, "")).strip() or None
                func = getattr(self, f"parse_{alias}", None)

                if func is not None:
                    item[alias] = func(value, data)
                else:
                    item[alias] = value

            # Parse any complex columns (dependent on more than one field)
            item["location"] = self.parse_location(data)
            item["images"] = self.parse_images(data)

            records.append(item)

        return records

    def parse_special_case(self, value, data):
        """Parse the SpecialCase from the raw data"""
        if not value:
            return None

        for key, label in SpecialCase.choices:
            if label == value:
                return key

        raise ValueError(f"Invalid special case: {value}")

    def parse_quick_description(self, value, data):
        """Parse the QuickDescription from the raw data"""
        if not value:
            return None

        for key, label in QuickDescription.choices:
            if label == value:
                return key

        raise ValueError(f"Invalid quick description: {value}")

    def parse_measured_at(self, value, data):
        """Parse the UTC CreationDate from the raw data"""
        measured_at = datetime.strptime(value, "%m/%d/%Y %H:%M")
        measured_at = measured_at.replace(tzinfo=timezone.utc)
        return measured_at

    def parse_location(self, data):
        """Parse the coordinate from the (x, y) values"""
        # FIXME: check longitude/latitude
        x = float(data["x"])
        y = float(data["y"])
        return Point(x, y)

    def parse_images(self, data):
        """Parse the list of images from the data"""
        # FIXME: update to support ArcGIS exports (currently not available)
        images = []

        for key in data:
            match = re.match("^Image Link(?P<count>\d+)$", key)

            if match is not None:
                count = match.group("count")
                image = {
                    "url": data[key],
                    "captured_at": data[f"Image Timestamp{count}"],
                }
                images.append(image)

        return images
