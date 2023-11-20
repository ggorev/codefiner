import os
import shutil
import tempfile

from src.service.gitlab.utils import get_file_from_repository


def test_get_file_from_repository():
    temp_dir = tempfile.mkdtemp()
    output_path = os.path.join(temp_dir, "gitlab-file.txt")
    get_file_from_repository("https://gitlab.com/gitlab-org/gitlab/-/blob/master/.foreman?ref_type=heads",
                             output=output_path)
    assert os.path.isfile(output_path)
    shutil.rmtree(temp_dir)
