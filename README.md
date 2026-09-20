# Particle Annihilation

Particle Annihilation is a small physics-focused Python project centered on electron-positron annihilation and related particle/wave calculations.

When an electron meets a positron, the pair can annihilate and convert their combined rest mass into energy according to Einstein's equation:

E = mc^2

For a standard electron-positron pair, the released energy is:

E = 2m_ec^2

This project includes a reusable Python module for:
- electron-positron annihilation energy
- photon energy from frequency
- photon energy from wavelength
- de Broglie wavelength calculations
- particle metadata for common atomic and subatomic particles

## Project structure

- `particle_annihilation.py` — core particle and wave calculations
- `app.py` — Flask API for cloud deployment
- `tests/test_particle_annihilation.py` — physics regression tests
- `Dockerfile` — container image for Cloud Run
- `requirements.txt` — Python runtime dependencies

## Local usage

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the module directly:

```bash
python -m particle_annihilation --mass 9.1093837015e-31 --photons 2
```

Run the Flask API locally:

```bash
python app.py
```

Then open:

```text
http://localhost:8080/
```

## Example API endpoints

```text
GET /
GET /particles
GET /particle/electron
GET /annihilation?mass_a=9.1093837015e-31&mass_b=9.1093837015e-31
GET /photon/energy?frequency_hz=5e14
GET /debroglie?mass_kg=9.1093837015e-31&velocity_m_s=1e5
```

## Google Cloud Run deployment

Build and deploy:

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

This project is intentionally focused on Particle Annihilation as the central concept, while also exposing supporting atomic and subatomic wave calculations in a compact, deployable form.
