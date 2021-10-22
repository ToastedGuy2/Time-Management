from ..utils.hasher import Hasher


class TestHasher:

    def test_hash_password_length_is_120(self):
        # Arrage
        password = "Hello_World"
        # Act
        hash = Hasher().hash_password(password)
        # Assert
        assert len(hash) is 120

    def test_verify_password_is_correct(self):
        # Arrage
        password = '1234'

        # Act
        hash = '$6$rounds=656000$pSnCZK5QK9nAx6Qw$IRLrA.JpHF9mZSiTIBAjgDcRHJWf6UU8APTYm5AvZcwAmvK6WJkDdfldrP228dmxQzI16WFax4kEG5fo5Bhdt1'

        # Assert
        assert Hasher().verify_password(password, hash)

    def test_verify_password_is_wrong(self):
        # Arrage
        password = '12345'

        # Act
        hash = '$6$rounds=656000$pSnCZK5QK9nAx6Qw$IRLrA.JpHF9mZSiTIBAjgDcRHJWf6UU8APTYm5AvZcwAmvK6WJkDdfldrP228dmxQzI16WFax4kEG5fo5Bhdt1'

        # Assert
        assert Hasher().verify_password(password, hash) is False
