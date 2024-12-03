import ufl
def test_ufl():
    r = ufl.FiniteElement("R", cell=ufl.triangle)
    assert r.sobolev_space() is ufl.L2