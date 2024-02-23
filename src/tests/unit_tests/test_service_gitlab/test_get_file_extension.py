from src.service.gitlab.utils import get_file_extension


def test_get_file_extension():
    assert get_file_extension(
        "https://gitlab.com/gitlab-org/gitlab/-/blob/master/scripts/api/base.rb?ref_type=heads") == '.rb'
