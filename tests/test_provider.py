from mcc import Lang, get_provider_class
from mcc.providers.go import MccabeGo
from mcc.providers.js import MccabeJS
from mcc.providers.python import MccabePy


def test_get_provider():
    assert get_provider_class(Lang.go) == MccabeGo
    assert get_provider_class(Lang.py) == MccabePy
    assert get_provider_class(Lang.js) == MccabeJS
