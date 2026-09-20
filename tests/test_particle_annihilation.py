import math

from particle_annihilation import (
    ELECTRON_MASS_KG,
    PLANCK_CONSTANT_J_S,
    SPEED_OF_LIGHT_M_S,
    PARTICLES,
    annihilation_energy,
    annihilation_energy_for_pair,
    de_broglie_wavelength,
    electron_positron_annihilation_energy,
    gamma_photon_energy,
    particle_data,
    photon_energy,
)


def test_default_annihilation_energy_matches_physics():
    expected = 2 * ELECTRON_MASS_KG * SPEED_OF_LIGHT_M_S ** 2
    assert math.isclose(annihilation_energy(), expected, rel_tol=1e-12)
    assert math.isclose(
        electron_positron_annihilation_energy(),
        expected,
        rel_tol=1e-12,
    )


def test_two_photons_each_receive_half_the_total_energy():
    total = annihilation_energy()
    each = gamma_photon_energy(total, 2)
    assert math.isclose(each, total / 2, rel_tol=1e-12)


def test_custom_masses_are_supported():
    mass = 1.0e-30
    expected = 2 * mass * SPEED_OF_LIGHT_M_S ** 2
    assert math.isclose(annihilation_energy(mass, mass), expected, rel_tol=1e-12)


def test_particle_catalog_includes_common_particles_and_waves():
    assert "electron" in PARTICLES
    assert "proton" in PARTICLES
    assert "photon" in PARTICLES
    assert particle_data("electron")["mass_kg"] == ELECTRON_MASS_KG


def test_photon_energy_uses_plancks_law():
    frequency = 5.0e14
    assert math.isclose(photon_energy(frequency), PLANCK_CONSTANT_J_S * frequency, rel_tol=1e-12)


def test_debroglie_wavelength_matches_formula():
    mass = 9.1093837015e-31
    velocity = 1.0e5
    expected = PLANCK_CONSTANT_J_S / (mass * velocity)
    assert math.isclose(de_broglie_wavelength(mass, velocity), expected, rel_tol=1e-12)


def test_annihilation_energy_for_a_known_pair():
    assert math.isclose(
        annihilation_energy_for_pair("electron", "positron"),
        electron_positron_annihilation_energy(),
        rel_tol=1e-12,
    )
