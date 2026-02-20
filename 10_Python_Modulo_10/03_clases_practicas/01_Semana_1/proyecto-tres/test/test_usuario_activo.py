import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.usuarios import es_usuario_activo

def test_usuario_activo_29_dias():
    ultimo_login_dias = 29
    resultado = es_usuario_activo(ultimo_login_dias)
    assert resultado is True

def test_usuario_activo_30_dias():
    ultimo_login_dias = 30
    resultado = es_usuario_activo(ultimo_login_dias)
    assert resultado is True

def test_usuario_inactivo_31_dias():
    ultimo_login_dias = 31
    resultado = es_usuario_activo(ultimo_login_dias)
    assert resultado is False

def test_valor_negativo():
    ultimo_login_dias = -1
    resultado = es_usuario_activo(ultimo_login_dias)
    assert resultado is True

def test_usuario_inactivo_un_anio():
    ultimo_login_dias = 365
    resultado = es_usuario_activo(ultimo_login_dias)
    assert resultado is False

def test_usuario_inactivo_valor_extremo():
    ultimo_login_dias = 99999
    resultado = es_usuario_activo(ultimo_login_dias)
    assert resultado is False