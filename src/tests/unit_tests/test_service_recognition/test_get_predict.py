from src.service.recognition.get_predict import get_predict


def test_get_predict():
    assert get_predict("using namespace std;").prediction['language'] == 'c++'
