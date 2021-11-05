from mcc.providers.go import MccabeGo
from mcc.providers.js import MccabeJS
from mcc.providers.python import MccabePy


def test_py_file():
    c = MccabePy(file="tests/sources/py.py")
    ret = c.run()
    assert ret == {"tests/sources/py.py": 24}


def test_py_dir():
    c = MccabePy(directory="tests")
    ret = c.run()
    assert ret == {
        "tests/test_languages.py": 9,
        "tests/__init__.py": 0,
        "tests/test_cyclomaticc_complexity.py": 8,
        "tests/sources/py.py": 24,
        "tests/test_provider.py": 4,
    }


def test_go():
    c = MccabeGo(file="tests/sources/go.go")
    ret = c.run()
    assert ret == {"tests/sources/go.go": 15}


def test_js():
    c = MccabeJS(file="tests/sources/js.js")
    ret = c.run()
    assert ret == {"tests/sources/js.js": 18}
