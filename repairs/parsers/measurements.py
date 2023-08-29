import csv

from repairs.models.constants import QuickDescription, SpecialCase


class MeasurementParser:
    """Measurement record parser for CSV file"""

    _columns = {
        "No.": "object_id",
        "H1": "h1",
        "H2": "h2",
        "Location": "address",
        "City": "city",
        "State": "state",
        "Country": "country",
        "Zip Code": "zip_code",
        "Special Case": "special_case",
        "Quick Description": "quick_description",
        "Lineal Feet": "lineal_feet",
        "Inch Feet": "inch_feet",
        "Cost": "cost",
        "Notes": "note",
        "Width": "width",
        "Length": "length",
        "Quality": "quality",
        "Date": "date",
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
            item["images"] = []

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

    def parse_location(self, data):
        """Parse the coordinate from the (x, y) values"""
        # FIXME: check longitude/latitude
        x = float(data["x"])
        y = float(data["y"])
        return (x, y)
