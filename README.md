
<img src="imgs/logo.png" height="100" width=auto>

# [Clinical-Data-Standardization-by-Developing-an-Interoperability-Framework](https://openreview.net/forum?id=Ayf90B1yESX)

### 

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
 <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

The Medkit-Learn(ing) Environment, or Medkit, is a publicly available Python package providing simple and easy access to high-fidelity synthetic medical data.

Primarily, Medkit is a tool that supports: (1) a variety of realistic environment models—learned from actual data, to reflect real medical settings), thus allowing simulation of (2) a variety of expressive and customisable policy models that represent complex human decision-behaviours; as well as (3) ensuring that the environment and policy components are disentangled—hence independently controllable.

By fulfilling the above, Medkit seeks to enable advances in decision modelling to be validated more easily and robustly by enabling users to obtain batch datasets with known ground-truth policy parameterisations that simulate decision making behaviours with various degrees of Markovianity, bounded rationality, confounding, individual consistency and variation in practice.

<p align="center">
    <img src="imgs/overview.png" height="180" width=auto>
</p>


The primary objectives of this research are to address the following potential issues with clinical data standardization in Bangladesh.
1) Inconsistency in clinical terminology and measurement.
2) No clinical registry code for EHR in Bangladesh eHealth standard.
3) Deter the process of consistent data integration in a central Big Data repositoryLack of interoperability data exchange format.
For clinical data standardization, which is required for information interchange and analytics, we are investigating and building an interoperability framework to map from custom codes to standard codes.


cd medkit-learn

pip install -e .
```

Alternatively, Medkit is available on [PyPI](https://pypi.org/project/medkit-learn/), and can be installed simply with:


Example usage:

While medical machine learning is by necessity almost always entirely offline, we also provide an interface through which you can interact online with the environment should you find that useful. For example, you could train a custom RL policy on this environment with a specified reward function, then you can test inference algorithms on their ability to represent the policy.

```python
env = mk.live_simulate(
    domain="ICU",
    environment="SVAE"
)

static_obs, observation, info = env.reset()
observation, reward, info, done = env.step(action)
```

### Citing

If you use this software please cite as follows:


