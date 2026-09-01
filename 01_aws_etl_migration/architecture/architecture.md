# Architecture Notes

## Components

- **EventBridge:** scheduling/trigger.
- **Step Functions:** workflow orchestration and processing-job monitoring.
- **SageMaker Processing:** managed compute for the Python ETL workload.
- **S3:** pipeline artifacts and inactive-data archive.
- **Secrets Manager:** runtime secrets.
- **Redshift:** active analytics-ready datasets.
- **Athena:** SQL access to archived S3 data.
- **CloudWatch:** centralized logs and operational visibility.

## Security and networking

For a private deployment, the processing job can be associated with the required VPC, subnets, and security groups. IAM controls authorization separately from network connectivity.

```text
IAM         -> Am I allowed?
VPC/network -> Can I reach it?
DB access   -> Can I perform the required SQL operation?
```
