import csv
import re


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
        "Quick Description": "quick_description",
        "Special Case": "special_case",
        "Lineal Feet": "lineal_feet",
        "Inch Feet": "inch_feet",
        "Cost": "cost",
        "Notes": "note",
        "Length": "length",
        "Width": "width",
        "Quality": "quality",
        "Date": "measured_at",
    }

    def parse(self, file_obj):
        """Parse the CSV file into a list of records"""
        file_obj.seek()
        measurements = []

        for item in csv.DictReader(file_obj, delimiter=","):
            measurement = {column: item.get(alias) for alias, column in self._columns}
            measurement["location"] = self.parse_location(item)
            measurement["images"] = self.parse_images(item)
            measurements.append(measurement)

        return measurements

    def parse_location(self, item):
        """Parse the Point coordinate from the raw item"""
        longitude = item["Y"]
        latitude = item["X"]
        return [float(longitude), float(latitude)]

    def parse_images(self, item):
        """Parse the images from the raw item"""
        images = []

        for key in item:
            match = re.match("^Image Link(\d+)$", key)

            if match:
                url = item[key]
                captured_at = item[f"Image Time Stamp{match.group(0)}"]
                images.append({"url": url, "captured_at": captured_at})

        return images
