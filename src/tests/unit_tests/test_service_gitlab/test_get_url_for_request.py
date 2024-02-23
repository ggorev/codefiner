import pytest

from src.service.exceptions import InvalidGitlabLinkException
from src.service.gitlab.utils import get_url_for_request


def test_get_url_for_request():
    assert get_url_for_request(
        "https://gitlab.com/gitlab-org/gitlab/-/blob/master/app/views/devise/registrations/edit.html.erb?ref_type=heads") == "https://gitlab.com/api/v4/projects/gitlab-org%2Fgitlab/repository/files/app%2Fviews%2Fdevise%2Fregistrations%2Fedit.html.erb?ref=master"


def test_get_url_for_request_invalid_link():
    with pytest.raises(InvalidGitlabLinkException):
        get_url_for_request("gitlab/gitlab-org/gitlab/-/blob/master/.gitignore?ref_type=heads")
