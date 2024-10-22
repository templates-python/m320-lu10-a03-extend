import pytest
from mobile import Mobile

class TestMobile:

    @pytest.fixture
    def a_mobile(self):
        return Mobile()

    def test_what_i_am_mobile(self, a_mobile):
        assert a_mobile.what_i_am() == 'an old mobile'

    def test_function_mobile(self, a_mobile, capsys):
        a_mobile.calling()
        a_mobile.handle_sms()
        captured = capsys.readouterr()
        assert captured.out == 'anrufen\nsms senden und empfangen\n'