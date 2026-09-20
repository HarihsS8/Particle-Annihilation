import os
from typing import Any

from flask import Flask, jsonify, request

from particle_annihilation import (
    PARTICLES,
    annihilation_energy,
    annihilation_energy_for_pair,
    de_broglie_wavelength,
    particle_data,
    photon_energy,
    photon_wavelength,
    wave_energy_from_wavelength,
)

app = Flask(__name__)


@app.get("/")
def index() -> Any:
    return jsonify(
        {
            "name": "Particle Annihilation",
            "description": "Atomic and subatomic particle and wave calculations",
            "endpoints": [
                "/particles",
                "/annihilation",
                "/photon/energy",
                "/photon/wavelength",
                "/debroglie",
            ],
        }
    )


@app.get("/particles")
def list_particles() -> Any:
    return jsonify({"particles": list(PARTICLES)})


@app.get("/particle/<name>")
def particle(name: str) -> Any:
    try:
        data = particle_data(name)
        return jsonify(data)
    except KeyError as exc:
        return jsonify({"error": str(exc)}), 404


@app.get("/annihilation")
def annihilation() -> Any:
    mass_a = float(request.args.get("mass_a", 9.1093837015e-31))
    mass_b = float(request.args.get("mass_b", 9.1093837015e-31))
    energy = annihilation_energy(mass_a, mass_b)
    return jsonify({"mass_a_kg": mass_a, "mass_b_kg": mass_b, "energy_j": energy})


@app.get("/annihilation/pair")
def annihilation_pair() -> Any:
    particle_a = request.args.get("particle_a", "electron")
    particle_b = request.args.get("particle_b")
    try:
        energy = annihilation_energy_for_pair(particle_a, particle_b)
        return jsonify({"particle_a": particle_a, "particle_b": particle_b or particle_a, "energy_j": energy})
    except Exception as exc:  # pragma: no cover - API guard
        return jsonify({"error": str(exc)}), 400


@app.get("/photon/energy")
def photon_energy_route() -> Any:
    frequency = float(request.args.get("frequency_hz", 1.0e14))
    return jsonify({"frequency_hz": frequency, "energy_j": photon_energy(frequency)})


@app.get("/photon/wavelength")
def photon_wavelength_route() -> Any:
    frequency = float(request.args.get("frequency_hz", 1.0e14))
    return jsonify({"frequency_hz": frequency, "wavelength_m": photon_wavelength(frequency)})


@app.get("/photon/energy-from-wavelength")
def photon_energy_from_wavelength_route() -> Any:
    wavelength = float(request.args.get("wavelength_m", 5.0e-7))
    return jsonify({"wavelength_m": wavelength, "energy_j": wave_energy_from_wavelength(wavelength)})


@app.get("/debroglie")
def debroglie() -> Any:
    mass = float(request.args.get("mass_kg", 9.1093837015e-31))
    velocity = float(request.args.get("velocity_m_s", 1.0e5))
    return jsonify({"mass_kg": mass, "velocity_m_s": velocity, "wavelength_m": de_broglie_wavelength(mass, velocity)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8080")), debug=False)
