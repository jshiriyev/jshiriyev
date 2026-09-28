# Hi, I'm Javid Shiriyev 👋

**Engineer building data, simulation & AI systems — Ph.D. (UT Austin), 10+ years of Python, energy domain.**

I've spent fifteen years building the models, data systems, and now AI pipelines that turn subsurface measurements into decisions. Across every role, the real deliverable has been software: inversion code in my Ph.D., a mesh-free solver in my postdoc, a well-data platform backend at a national oil company, and now production LLM-agent pipelines.

📍 Coppell, TX (Dallas–Fort Worth)

## What I'm working on

- 🤖 **Production LLM-agent pipeline for well-data QC.** It is shipped as a Claude Code plugin (three chained skills) and does the following:
  - multi-jurisdiction document retrieval
  - grounded extraction with per-document provenance
  - an append-only evidence store
  - deterministic SQL conflict resolution (no LLM in the tie-break)
  - geometry validation and staged human sign-off

  It has been validated on ~500 wells.
- 🔗 **Acquisition deal-integration pipeline.** A quarterly Python pipeline that drives a reserves-software REST API end to end: entity resolution against PostgreSQL, an identifier crosswalk, and automated underwriting-vs-booked reconciliation.
- 🗄️ **Sand-Control Failure Database** *(private)*. Sole data engineer for a UT Austin research consortium: schema design, ingestion, and query system, with data contributed by 10 major operators.
- 📚 **[Data Science Guide](https://jshiriyev.github.io/data-science-guide/).** A cheat-sheet site covering statistics, Python, ML, big data and deep learning, with one new sheet each week.

## Featured projects

| Project | What it is | Stack |
|---|---|---|
| [**production-data-analysis**](https://github.com/jshiriyev/production-data-analysis) · [`prodpy` on PyPI](https://pypi.org/project/prodpy/) | Production forecasting toolkit: vectorized Arps decline-curve fitting with uncertainty sampling, multi-zone production allocation, one-page production dashboards | Python, NumPy, SciPy, pandas, Matplotlib |
| [**formation-evaluation**](https://github.com/jshiriyev/formation-evaluation) (`pphys`) | Well-log interpretation: LAS file QC and PDF reports (`LasView`), interactive Bokeh log viewer, one-page well and cross-section views, shaly-sand porosity and saturation models | Python, Bokeh, Matplotlib, uv |
| [**wellx-webapp**](https://github.com/jshiriyev/wellx-webapp) | Web app for field data: map-based well explorer, time-series and decline dashboards, petrophysics and flow modules behind a validated API | FastAPI, Pydantic, Vue, Leaflet, Vite |
| [**data-science-guide**](https://github.com/jshiriyev/data-science-guide) | Static cheat-sheet site with automated catalog generation, link checks, and GitHub Pages deploys | HTML/CSS/JS, Python, GitHub Actions |

## Background

- **Ph.D., Petroleum Engineering — The University of Texas at Austin** (advisor: Mukul Sharma). Built the forward electromagnetic simulators and the simulated-annealing inversion for a DOE-funded fracture-diagnostics tool.
- **Postdoc, UT Austin.** Boundary-element / integral-equation solver as a fast, mesh-free alternative to FEM/FDM for real-time flow modeling.
- **SOCAR Upstream — Field Development Lead & Data Management.** Wrote the entire backend of a Vue/FastAPI/PostgreSQL well-data platform used by 50+ engineers, and built dashboards that 80% of the reservoir team adopted.
- **Six years teaching** reservoir simulation and petrophysics (Baku Higher Oil School, METU NCC). Supervised 50+ theses.
- **B.Sc. & M.Sc., Middle East Technical University.** Ranked first in the department.

## Tech stack

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?logo=pydantic&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?logo=sqlalchemy&logoColor=white)
![Vue.js](https://img.shields.io/badge/Vue.js-4FC08D?logo=vuedotjs&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?logo=scipy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?logo=plotly&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-E25A1C?logo=apachespark&logoColor=white)
![Claude Code](https://img.shields.io/badge/Claude%20Code-D97757?logo=claude&logoColor=white)
![QGIS](https://img.shields.io/badge/QGIS-589632?logo=qgis&logoColor=white)
![MATLAB](https://img.shields.io/badge/MATLAB-0076A8?logo=mathworks&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?logo=pytest&logoColor=white)

**Domain tools:** tNavigator · CMG · Eclipse · Petrel · Techlog · ComboCurve · Enverus · Spotfire

## Selected publications

- Shiriyev et al. (2018). *Experiments and simulations of a prototype triaxial electromagnetic induction logging tool for open-hole hydraulic fracture diagnostics.* **Geophysics**, 83(3), D73–D81.
- Zhang, Shiriyev et al. (2019). *Fast inversion of downhole electrical measurements for proppant mapping using very fast simulated annealing.* **Geophysics**, 85(1).
- Shiriyev et al. (2023). *Evaluating the optimal logging suite for sandstone reservoirs in the South Caspian Basin.* SPE Caspian Technical Conference.

Full list: [Google Scholar](https://scholar.google.com/citations?user=YvggY5wAAAAJ&hl=en)

## GitHub stats

<p>
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=jshiriyev&show_icons=true&count_private=true&hide_border=true" alt="Javid's GitHub stats" />
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=jshiriyev&layout=compact&hide_border=true" alt="Top languages" />
</p>

## 📫 Get in touch

- 📧 [jshiriyev.longhorn@gmail.com](mailto:jshiriyev.longhorn@gmail.com)
- 🔗 [LinkedIn](https://www.linkedin.com/in/jshiriyev/)
- 🌐 [jshiriyev.github.io](https://jshiriyev.github.io)
- 🎓 [Google Scholar](https://scholar.google.com/citations?user=YvggY5wAAAAJ&hl=en)
