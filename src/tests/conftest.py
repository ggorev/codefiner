import os

import pytest


@pytest.fixture(autouse=True, scope="session")
def create_file_for_test():
    with open("cpp.txt", 'w') as f:
        f.write("using namespace std;")
    yield
    os.remove("cpp.txt")
