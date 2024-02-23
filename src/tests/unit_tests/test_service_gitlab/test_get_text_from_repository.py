from src.service.gitlab.utils import get_text_from_repository


def test_get_text_from_repository():
    assert get_text_from_repository(
        "https://gitlab.com/gitlab-org/gitlab/-/blob/master/.foreman?ref_type=heads") == "port: 3000\n"
