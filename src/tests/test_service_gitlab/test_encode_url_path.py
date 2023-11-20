from src.service.gitlab.utils import encode_url_path


def test_encode_url_path():
    assert encode_url_path("src/service/gitlab/utils") == "src%2Fservice%2Fgitlab%2Futils"
