# Jenkins Configuration

This folder contains all Jenkins-related configuration files for the trading-bot project.  
It centralizes the automation of data ingestion, model training, signal generation, and live execution workflows.

## Structure

- **Jenkinsfiles**: Scripted pipelines controlling the execution of various project components.
- **Jobs**: Each job corresponds to a specific function (data ingestion, model training, signal generation, trade execution).
- **Configuration Files**: Settings related to Jenkins pipelines are stored here to maintain Infrastructure-as-Code principles.

## Pipelines Overview

Each trading component is organized as an independent Jenkins pipeline:

| Pipeline                | Purpose                                       |
|:-------------------------|:----------------------------------------------|
| Data Ingestion           | Pull market data, macroeconomic data, news    |
| Model Research/Training  | Train and backtest strategies offline         |
| Signal Generation        | Detect trading opportunities based on models |
| Execution                | Send trade orders via Interactive Brokers API |

## Execution Flow

1. **Checkout**: Pulls the latest code from the Git repository.
2. **Environment Setup**: Creates/uses a Python virtual environment inside the workspace.
3. **Dependency Installation**: Installs Python libraries from `requirements.txt`.
4. **Script Execution**: Runs the relevant Python script for the pipeline stage.
5. **Logging**: Logs outputs for monitoring and debugging.

All pipelines are **scripted** (not declarative) for maximum control and flexibility.

## Best Practices

- Keep all Jenkins-related files inside the `jenkins/` folder.
- Each pipeline should have a clean, dedicated Jenkinsfile.
- Follow modular architecture: ingestion, models, signals, execution are separate.
- Pipelines should fail loudly and early if something goes wrong (no silent failures).
- Environment setup should always be handled inside the pipeline to ensure repeatability.

## Notes

- **Docker** is intentionally **not** used at this stage to minimize overhead and maximize development speed.
- **Kubernetes** orchestration is **not** required at this stage.  
  Future migration to containers/orchestration will be considered once the system scales.

## Future Improvements

- Integrate Jenkins Configuration-as-Code (JCasC) for full environment automation.
- Implement monitoring and alerting for failed pipelines.
- Consider containerization (Docker) when scaling becomes necessary.
