import json
import csv
import os

import pytest

from storage_classes.storage_json import StorageJson
from storage_classes.storage_csv import StorageCsv


@pytest.fixture(autouse=True)
def storage():
    with open("test.json", "w") as handle:
        handle.write(json.dumps(
            {"Moana": {"year": 2016, "rating": 7.6, "poster": "poster"}}))
    with open("test.csv", "w") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=["title", "year", "rating", "poster"])
        writer.writeheader()
        writer.writerow({"title": "Moana", "year": 2016, "rating": 7.6,
                         "poster": "poster"})

    yield StorageJson("test.json"), StorageCsv("test.csv")
    os.remove("test.json")
    os.remove("test.csv")


def test_add_movie(storage):
    for storage_type in storage:
        storage_type.add_movie("Mulan", "1998", 7.6, "poster")
        assert len(storage_type.list_movies()) == 2


def test_delete_movie(storage):
    for storage_type in storage:
        storage_type.delete_movie("Moana")
        assert not len(storage_type.list_movies())
