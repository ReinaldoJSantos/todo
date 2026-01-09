import pytest
from app.core.security import hash_password, verify_password, validate_password_length


def test_validate_password_length_valid():
    """Testa se senhas com tamanho válido (<= 72 bytes) são aceitas."""
    password = "valid_password_123"
    # Não deve levantar exceção
    validate_password_length(password)

    # Limite exato
    limit_password = "a" * 72
    validate_password_length(limit_password)


def test_validate_password_length_invalid():
    """Testa se senhas muito longas (> 72 bytes) levantam ValueError."""
    long_password = "a" * 73
    with pytest.raises(ValueError) as excinfo:
        validate_password_length(long_password)
    assert "Senha deve ter no máximo 72 caracteres" in str(excinfo.value)


def test_hash_password_works():
    """Testa se o hash é gerado corretamente."""
    password = "secret_password"
    hashed = hash_password(password)

    assert hashed != password
    assert isinstance(hashed, str)
    # Verifica se é um hash bcrypt válido (passlib geralmente usa $2b$)
    assert hashed.startswith("$2b$")


def test_hash_password_validates_length():
    """Testa se hash_password também valida o tamanho antes de hashear."""
    long_password = "a" * 73
    with pytest.raises(ValueError):
        hash_password(long_password)


def test_verify_password_correct():
    """Testa verificação de senha correta."""
    password = "my_secure_password"
    hashed = hash_password(password)
    assert verify_password(password, hashed) is True


def test_verify_password_incorrect():
    """Testa verificação de senha incorreta e tratamento de inputs longos."""
    password = "my_secure_password"
    hashed = hash_password(password)
    assert verify_password("wrong_password", hashed) is False

    # Input longo na verificação deve retornar False (segurança)
    long_input = "a" * 73
    assert verify_password(long_input, hashed) is False