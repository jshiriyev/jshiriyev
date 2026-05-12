# jshiriyev
 
A focused ecosystem of reservoir-engineering tools for **production data analysis**, **formation evaluation**, and **field-data web delivery**.
 
## Vision
 
The goal of my project space is to provide practical, transparent, and reusable software for reservoir and production engineering workflows:
 
- Fast diagnostics from production history.
- Robust decline-curve and transient-analysis workflows.
- Reservoir property and PVT-related engineering utilities.
- Formation-level interpretation support.
- Web-based delivery of engineering results to broader teams.
 
Together, these repositories are intended to reduce manual spreadsheet work, improve reproducibility, and accelerate decision cycles.
 
## Repository Map
 
### 1) `production-data-analysis`
Core Python toolkit for production and reservoir-engineering calculations, including:

- Decline-curve analysis (Arps variants and related utilities).
- Production allocation and schedule-centric workflows.
- Reservoir property modules (fluid, rock, relative permeability, capillary pressure).
- Wellbore flow utilities (single-phase and two-phase contexts).
- Material balance, transient analysis (PTA & RTA), and porous-media simulation components.

> Overall readiness: ~6/10

### 2) `formation-evaluation`
A companion repository for petrophysical and formation interpretation workflows (project-level positioning):

- Log-based formation quality screening.
- Pay identification and interval ranking.
- Integration-ready outputs for reservoir modeling and completion planning.
 
> Overall readiness: ~6/10
 
### 3) `wellx-webapp`
A web application layer for operationalizing engineering insights:
 
- Visual dashboards for production and reservoir diagnostics.
- Collaboration-friendly interfaces for engineers and asset teams.
- Potential APIs/services to connect analytics outputs with end-user tools.
 
> Overall readiness: ~6/10
 
## How These Repositories Work Together
 
A typical workflow across the ecosystem:
 
1. **Ingest field data & run engineering calculations (DCA | PTA | RTA)** in `production-data-analysis`.
2. **Cross-check subsurface intervals** and petrophysical context in `formation-evaluation`.
3. **Publish dashboards and decision views** via `wellx-webapp`.
 
This separation keeps each codebase focused while allowing clear integration points.

## Design Principles
 
- **Engineering-first**: methods should reflect real reservoir workflows.
- **Transparent math**: equations and assumptions should be inspectable.
- **Reproducible outputs**: code and notebooks over one-off manual analysis.
- **Composable modules**: small building blocks that can be chained into larger studies.
- **Practical adoption**: interfaces that support both technical experts and downstream stakeholders.


## Quick Start (this repository)

```bash
python -m pip install -U pip
python -m pip install -e .
 ```
 
Run tests:
 
 ```bash
 pytest -q
 ```
 
Explore examples in:

- `docs/`
 
 ## Contributing

Contributions and collaboration ideas are welcome. If you are working on reservoir-engineering workflows and would like to align methods, validation datasets, or tooling patterns, feel free to open an issue or pull request.

## 📫 Get in Touch

Feel free to reach out to me via:
- 📧 Email: jshiriyev.longhorn@gmail.com
- 🔗 LinkedIn: [click](https://www.linkedin.com/in/jshiriyev/)
 
 ## License

This project is licensed under the MIT License (see `LICENSE`).
