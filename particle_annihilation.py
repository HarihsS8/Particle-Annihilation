"""Physics calculations for atomic and subatomic particles and waves.

This module covers the most common particle masses and core wave/energy formulas,
including photon energy, de Broglie wavelength, and pair annihilation.
"""

from __future__ import annotations

import argparse

ELECTRON_MASS_KG = 9.1093837015e-31
POSITRON_MASS_KG = ELECTRON_MASS_KG
PROTON_MASS_KG = 1.67262192369e-27
NEUTRON_MASS_KG = 1.67492749804e-27
SPEED_OF_LIGHT_M_S = 299_792_458.0
PLANCK_CONSTANT_J_S = 6.62607015e-34
REDUCED_PLANCK_CONSTANT_J_S = PLANCK_CONSTANT_J_S / (2.0 * 3.141592653589793)
ELECTRON_CHARGE_C = 1.602176634e-19

PARTICLE_LIBRARY = {
    "electron": {
        "symbol": "e-",
        "mass_kg": ELECTRON_MASS_KG,
        "charge_c": -ELECTRON_CHARGE_C,
        "category": "lepton",
        "antiparticle": "positron",
    },
    "positron": {
        "symbol": "e+",
        "mass_kg": POSITRON_MASS_KG,
        "charge_c": ELECTRON_CHARGE_C,
        "category": "antilepton",
        "antiparticle": "electron",
    },
    "proton": {
        "symbol": "p+",
        "mass_kg": PROTON_MASS_KG,
        "charge_c": ELECTRON_CHARGE_C,
        "category": "baryon",
        "antiparticle": "antiproton",
    },
    "antiproton": {
        "symbol": "p-",
        "mass_kg": PROTON_MASS_KG,
        "charge_c": -ELECTRON_CHARGE_C,
        "category": "antibaryon",
        "antiparticle": "proton",
    },
    "neutron": {
        "symbol": "n",
        "mass_kg": NEUTRON_MASS_KG,
        "charge_c": 0.0,
        "category": "baryon",
        "antiparticle": "antineutron",
    },
    "antineutron": {
        "symbol": "n̄",
        "mass_kg": NEUTRON_MASS_KG,
        "charge_c": 0.0,
        "category": "antibaryon",
        "antiparticle": "neutron",
    },
    "photon": {
        "symbol": "γ",
        "mass_kg": 0.0,
        "charge_c": 0.0,
        "category": "boson",
        "antiparticle": "photon",
    },
    "muon": {
        "symbol": "μ-",
        "mass_kg": 1.883531627e-28,
        "charge_c": -ELECTRON_CHARGE_C,
        "category": "lepton",
        "antiparticle": "antimuon",
    },
    "antimuon": {
        "symbol": "μ+",
        "mass_kg": 1.883531627e-28,
        "charge_c": ELECTRON_CHARGE_C,
        "category": "antilepton",
        "antiparticle": "muon",
    },
    "tau": {
        "symbol": "τ-",
        "mass_kg": 3.16754e-27,
        "charge_c": -ELECTRON_CHARGE_C,
        "category": "lepton",
        "antiparticle": "antitau",
    },
    "antitau": {
        "symbol": "τ+",
        "mass_kg": 3.16754e-27,
        "charge_c": ELECTRON_CHARGE_C,
        "category": "antilepton",
        "antiparticle": "tau",
    },
    "neutrino": {
        "symbol": "ν",
        "mass_kg": 2.2e-36,
        "charge_c": 0.0,
        "category": "lepton",
        "antiparticle": "antineutrino",
    },
    "antineutrino": {
        "symbol": "ν̄",
        "mass_kg": 2.2e-36,
        "charge_c": 0.0,
        "category": "antilepton",
        "antiparticle": "neutrino",
    },
    "pion": {
        "symbol": "π",
        "mass_kg": 2.488e-28,
        "charge_c": 0.0,
        "category": "meson",
        "antiparticle": "antipion",
    },
    "antipion": {
        "symbol": "π̄",
        "mass_kg": 2.488e-28,
        "charge_c": 0.0,
        "category": "meson",
        "antiparticle": "pion",
    },
    "alpha": {
        "symbol": "α",
        "mass_kg": 6.6446573357e-27,
        "charge_c": 2.0 * ELECTRON_CHARGE_C,
        "category": "nucleus",
        "antiparticle": "alpha",
    },
    "deuteron": {
        "symbol": "d",
        "mass_kg": 3.3435837724e-27,
        "charge_c": ELECTRON_CHARGE_C,
        "category": "nucleus",
        "antiparticle": "deuteron",
    },
    "triton": {
        "symbol": "t",
        "mass_kg": 5.007356e-27,
        "charge_c": ELECTRON_CHARGE_C,
        "category": "nucleus",
        "antiparticle": "triton",
    },
    "hydrogen_atom": {
        "symbol": "H",
        "mass_kg": 1.673557e-27,
        "charge_c": 0.0,
        "category": "atom",
        "antiparticle": "hydrogen_ion",
    },
    "hydrogen_ion": {
        "symbol": "H+",
        "mass_kg": 1.67262192369e-27,
        "charge_c": ELECTRON_CHARGE_C,
        "category": "ion",
        "antiparticle": "hydrogen_atom",
    },
    "helium_atom": {
        "symbol": "He",
        "mass_kg": 6.64648e-27,
        "charge_c": 0.0,
        "category": "atom",
        "antiparticle": "helium_atom",
    },
    "up_quark": {
        "symbol": "u",
        "mass_kg": 2.2e-30,
        "charge_c": 2.0 / 3.0 * ELECTRON_CHARGE_C,
        "category": "quark",
        "antiparticle": "up_antiquark",
    },
    "up_antiquark": {
        "symbol": "ū",
        "mass_kg": 2.2e-30,
        "charge_c": -2.0 / 3.0 * ELECTRON_CHARGE_C,
        "category": "antiquark",
        "antiparticle": "up_quark",
    },
    "down_quark": {
        "symbol": "d",
        "mass_kg": 4.7e-30,
        "charge_c": -1.0 / 3.0 * ELECTRON_CHARGE_C,
        "category": "quark",
        "antiparticle": "down_antiquark",
    },
    "down_antiquark": {
        "symbol": "d̄",
        "mass_kg": 4.7e-30,
        "charge_c": 1.0 / 3.0 * ELECTRON_CHARGE_C,
        "category": "antiquark",
        "antiparticle": "down_quark",
    },
}

PARTICLES = tuple(sorted(PARTICLE_LIBRARY.keys()))

__all__ = [
    "ELECTRON_MASS_KG",
    "POSITRON_MASS_KG",
    "PROTON_MASS_KG",
    "NEUTRON_MASS_KG",
    "SPEED_OF_LIGHT_M_S",
    "PLANCK_CONSTANT_J_S",
    "REDUCED_PLANCK_CONSTANT_J_S",
    "ELECTRON_CHARGE_C",
    "PARTICLE_LIBRARY",
    "PARTICLES",
    "annihilation_energy",
    "annihilation_energy_for_pair",
    "de_broglie_wavelength",
    "electron_positron_annihilation_energy",
    "gamma_photon_energy",
    "pair_annihilation_energy",
    "particle_data",
    "photon_energy",
    "photon_wavelength",
    "wave_energy_from_wavelength",
]


def particle_data(name: str) -> dict:
    """Return metadata for a supported particle or wave-type label."""
    normalized = name.strip().lower().replace("-", "_")
    if normalized not in PARTICLE_LIBRARY:
        raise KeyError(f"Unknown particle or wave '{name}'. Supported: {', '.join(PARTICLES)}")
    return PARTICLE_LIBRARY[normalized].copy()


def annihilation_energy(
    electron_mass_kg: float = ELECTRON_MASS_KG,
    positron_mass_kg: float = POSITRON_MASS_KG,
) -> float:
    """Return total energy from converting mass into energy via E = mc^2."""
    if electron_mass_kg < 0 or positron_mass_kg < 0:
        raise ValueError("Mass values must be non-negative.")
    return (electron_mass_kg + positron_mass_kg) * SPEED_OF_LIGHT_M_S ** 2


def electron_positron_annihilation_energy(
    electron_mass_kg: float = ELECTRON_MASS_KG,
) -> float:
    """Return the energy released by a standard electron-positron pair."""
    return annihilation_energy(electron_mass_kg, electron_mass_kg)


def gamma_photon_energy(total_energy_joules: float, photon_count: int = 2) -> float:
    """Split a total energy evenly among a number of gamma photons."""
    if photon_count <= 0:
        raise ValueError("photon_count must be a positive integer.")
    return total_energy_joules / photon_count


def photon_energy(frequency_hz: float) -> float:
    """Return the energy of a photon using E = h f."""
    if frequency_hz < 0:
        raise ValueError("Frequency must be non-negative.")
    return PLANCK_CONSTANT_J_S * frequency_hz


def photon_wavelength(frequency_hz: float) -> float:
    """Return the wavelength of a photon in meters from its frequency."""
    if frequency_hz <= 0:
        raise ValueError("Frequency must be positive.")
    return SPEED_OF_LIGHT_M_S / frequency_hz


def wave_energy_from_wavelength(wavelength_m: float) -> float:
    """Return the energy of a photon from its wavelength using E = hc / λ."""
    if wavelength_m <= 0:
        raise ValueError("Wavelength must be positive.")
    return (PLANCK_CONSTANT_J_S * SPEED_OF_LIGHT_M_S) / wavelength_m


def de_broglie_wavelength(mass_kg: float, velocity_m_s: float) -> float:
    """Return the de Broglie wavelength λ = h / (mv)."""
    if mass_kg <= 0:
        raise ValueError("Mass must be positive.")
    if velocity_m_s < 0:
        raise ValueError("Velocity must be non-negative.")
    if velocity_m_s == 0:
        raise ValueError("Velocity must be greater than zero to define a wavelength.")
    return PLANCK_CONSTANT_J_S / (mass_kg * velocity_m_s)


pair_annihilation_energy = electron_positron_annihilation_energy


def annihilation_energy_for_pair(particle_a, particle_b=None) -> float:
    """Compute annihilation energy for a particle-antiparticle pair.

    Examples:
        annihilation_energy_for_pair("electron", "positron")
        annihilation_energy_for_pair("proton", "antiproton")
    """
    if isinstance(particle_a, str):
        particle_a_data = particle_data(particle_a)
        m1 = float(particle_a_data["mass_kg"])
    else:
        m1 = float(particle_a)

    if particle_b is None:
        if isinstance(particle_a, str):
            m2 = m1
        else:
            raise ValueError("A second mass or particle name is required when passing numeric mass values.")
    elif isinstance(particle_b, str):
        particle_b_data = particle_data(particle_b)
        m2 = float(particle_b_data["mass_kg"])
    else:
        m2 = float(particle_b)

    return annihilation_energy(m1, m2)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Calculate atomic and subatomic particle energies and wave properties."
    )
    parser.add_argument("--particle", choices=PARTICLES, default="electron", help="Particle to inspect.")
    parser.add_argument("--mass", type=float, default=None, help="Custom mass in kg for a pair calculation.")
    parser.add_argument("--other-particle", choices=PARTICLES, default=None, help="Companion particle for annihilation.")
    parser.add_argument("--frequency", type=float, default=None, help="Photon frequency in Hz.")
    parser.add_argument("--velocity", type=float, default=None, help="Particle velocity in m/s for de Broglie wavelength.")
    parser.add_argument("--wavelength", type=float, default=None, help="Photon wavelength in meters.")
    parser.add_argument("--photons", type=int, default=2, help="Number of equal-energy photons to split among.")
    args = parser.parse_args()

    particle = particle_data(args.particle)
    print(f"Particle: {args.particle} ({particle['symbol']})")
    print(f"Mass: {particle['mass_kg']:.12e} kg")
    print(f"Charge: {particle['charge_c']:.12e} C")

    if args.frequency is not None:
        energy = photon_energy(args.frequency)
        print(f"Photon energy: {energy:.12e} J")

    if args.wavelength is not None:
        wave_energy = wave_energy_from_wavelength(args.wavelength)
        print(f"Photon energy from wavelength: {wave_energy:.12e} J")

    if args.velocity is not None:
        lam = de_broglie_wavelength(particle["mass_kg"], args.velocity)
        print(f"De Broglie wavelength: {lam:.12e} m")

    if args.mass is not None:
        total = annihilation_energy(args.mass, args.mass)
        per_photon = gamma_photon_energy(total, args.photons)
        print(f"Total annihilation energy: {total:.12e} J")
        print(f"Per photon energy: {per_photon:.12e} J")
    elif args.other_particle is not None:
        total = annihilation_energy_for_pair(args.particle, args.other_particle)
        per_photon = gamma_photon_energy(total, args.photons)
        print(f"Total annihilation energy: {total:.12e} J")
        print(f"Per photon energy: {per_photon:.12e} J")
    else:
        total = annihilation_energy_for_pair(args.particle, args.particle)
        per_photon = gamma_photon_energy(total, args.photons)
        print(f"Total annihilation energy: {total:.12e} J")
        print(f"Per photon energy: {per_photon:.12e} J")


if __name__ == "__main__":
    main()
