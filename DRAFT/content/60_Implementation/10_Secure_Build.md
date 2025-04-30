## Secure Build

==DRAFT==

### Objectives
Establish secure integration of AI/LLM components by promoting responsible sourcing, secure coding, resilient design, and defensible supply chain choices.

| ⠀**Maturity Level** |                                             **Stream A – Process-Oriented**                                             | **Stream B – Technical Controls**                                                                                              |
|:-------------------:|:-----------------------------------------------------------------------------------------------------------------------:|--------------------------------------------------------------------------------------------------------------------------------|
|     **Level 1**     |          AI Model Inventory:- Maintain documented AI inventory.- Track sources and intended use of each model.          | Dependency and Licensing Checks:- Scan for known vulnerabilities.- Verify license terms and compliance.                        |
|     **Level 2**     | Secure AI Development Guidelines:- Define secure coding and data handling practices.- Perform AI-specific code reviews. | AI Component Hardening:- Implement input/output sanitization.- Use version control for models and datasets.- Validate outputs. |
|     **Level 3**     |      AI Supply Chain Risk Management:- Conduct risk assessments.- Maintain asset custody and request attestations.      | Adversarial Robustness and Resilience:- Perform adversarial testing.- Integrate checks in CI/CD.- Test edge-case behavior.     |

### Metrics
* Percentage of AI components with complete inventory and source validation
* Number of AI-related vulnerabilities identified pre-deployment
* Coverage of adversarial robustness testing across deployed models