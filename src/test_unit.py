import encrypt

def test_md5encrypt():
    assert "098f6bcd4621d373cade4e832627b4f6" == encrypt.md5("test")