import pytest

from mcc import languages
from mcc.languages import Lang


def test_convert():
    assert Lang.py == Lang("py")
    assert Lang.go == Lang("go")
    assert Lang.js == Lang("js")
    assert Lang.cpp == Lang("cpp")
    with pytest.raises(ValueError):
        Lang("xxx")


def test_get_lib():
    assert Lang.py.get_lib() == languages.PY_LANGUAGE
    assert Lang.go.get_lib() == languages.GO_LANGUAGE
    assert Lang.js.get_lib() == languages.JS_LANGUAGE
    assert Lang.cpp.get_lib() == languages.CPP_LANGUAGE
