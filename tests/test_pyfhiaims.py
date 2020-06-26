import pytest  # type: ignore

from fhiaims.errors import InvalidInput
from fhiaims.inputs import Aims, SpeciesDefaults
from fhiaims.outputs import parse_aims


def add_radial_base(species_defs, kwargs):
    for spec in species_defs:
        spec["radial_base"]["number"] += kwargs.pop("radial_base_add")


def test_inputs(shared_datadir):
    aims = Aims()
    SpeciesDefaults(add_radial_base)(aims)
    inputs = aims(
        species_defaults="light",
        atoms=[("Ar", 0, 0, 0)],
        radial_base_add=5,
        tags=dict(
            xc="pbe",
            relativistic="atomic_zora scalar",
            many_body_dispersion={"old_hirshfeld": True},
            dry_run=(),
            sc_accuracy_eev=1e-4,
            sc_accuracy_rho=1e-6,
            sc_accuracy_etot=1e-7,
            sc_iter_limit=100,
        ),
    )
    assert (
        inputs["control.in"].split()
        == (shared_datadir / "control.in").read_text().split()
    )
    assert (
        inputs["geometry.in"].split()
        == (shared_datadir / "geometry.in").read_text().split()
    )


def test_outputs(shared_datadir):
    with (shared_datadir / "aims.out").open() as f:
        results = parse_aims(f)
    assert results["total_energy"] == -63.4840264391664


def test_plugin_error():
    aims = Aims()
    with pytest.raises(KeyError):
        aims()


def test_unknown_kwargs():
    aims = Aims()
    with pytest.raises(InvalidInput):
        aims(species_defaults="light", atoms=[("Ar", 0, 0, 0)], tags={}, _unknown=None)


def test_double_call():
    aims = Aims()
    aims(species_defaults="light", atoms=[("Ar", 0, 0, 0)], tags={})
    aims(species_defaults="light", atoms=[("Ar", 0, 0, 0)], tags={})
