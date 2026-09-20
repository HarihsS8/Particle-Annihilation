# Particle Annihilation

## Abstract

Particle Annihilation is a computational physics project designed to model electron-positron annihilation and related atomic and subatomic wave phenomena. The central process examined is the conversion of matter into radiation when a particle and its antiparticle interact. This project implements the governing physical relationships in a reproducible software framework and provides a deployable interface for calculation and analysis.

## Theory

When an electron and a positron meet, they undergo mutual annihilation. In this process, both particles cease to exist as independent matter states. Their combined rest mass is converted into energy according to the relativistic mass-energy equivalence relation:

$$E = mc^2$$

For a standard electron-positron pair, the total released energy is:

$$E_{total} = 2m_ec^2$$

For the canonical two-photon annihilation channel, the released energy is shared approximately equally between two gamma photons:

$$E_{\gamma} = \frac{E_{total}}{2}$$

Additional relationships implemented in the project include:

- Photon energy: $E = hf$
- Photon wavelength: $\lambda = c/f$
- Photon energy from wavelength: $E = hc/\lambda$
- De Broglie wavelength: $\lambda = h/(mv)$

## Methodology

The project provides a Python implementation of the relevant equations and stores reference values for common subatomic and atomic particles. Calculations are organized in a modular form to allow direct evaluation of annihilation energy, electromagnetic radiation energy, and wave properties.

### Computational modules

- `particle_annihilation.py` — core physical calculations
- `app.py` — Flask application for API access and deployment
- `tests/test_particle_annihilation.py` — regression tests verifying expected behavior
- `Dockerfile` — container definition for Google Cloud Run
- `requirements.txt` — project dependencies

## Local execution

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the calculation module directly:

```bash
python -m particle_annihilation --mass 9.1093837015e-31 --photons 2
```

Start the local API service:

```bash
python app.py
```

The service is available at:

```text
http://localhost:8080/
```

## API endpoints

```text
GET /
GET /particles
GET /particle/electron
GET /annihilation?mass_a=9.1093837015e-31&mass_b=9.1093837015e-31
GET /photon/energy?frequency_hz=5e14
GET /debroglie?mass_kg=9.1093837015e-31&velocity_m_s=1e5
```

## Results

For a standard electron-positron annihilation event using the electron rest mass:

- Total energy released: $1.637421155365 \times 10^{-13}$ J
- Energy per gamma photon (two-photon case): $8.187105776824 \times 10^{-14}$ J

These values are consistent with the mass-energy equivalence relation and the assumption of a symmetric two-photon final state.

## Deployment

Build and deploy to Google Cloud Run:

```bash
export PROJECT_ID="your-gcp-project-id"
export REGION="us-central1"
export SERVICE_NAME="particle-annihilation"

gcloud config set project "$PROJECT_ID"
gcloud builds submit --tag gcr.io/"$PROJECT_ID"/"$SERVICE_NAME"
gcloud run deploy "$SERVICE_NAME" \
  --image gcr.io/"$PROJECT_ID"/"$SERVICE_NAME" \
  --platform managed \
  --region "$REGION" \
  --allow-unauthenticated
```

## Verification

Run the test suite:

```bash
pytest -q
```

## Conclusion

This project provides a compact, deployable scientific framework for the study of particle annihilation and related atomic and subatomic wave calculations. It is intended as a practical computational reference for the standard relationships governing annihilation, radiation, and quantum wave behavior.
