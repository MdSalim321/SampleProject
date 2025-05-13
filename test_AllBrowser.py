import pytest

@pytest.mark.usefixtures
def test_CrossBrowser(crossBrowser):
    print(crossBrowser[1])
