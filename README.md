# aws-vcf-env

Envrionment for working with AWS VCFs

## Getting started

1. Ensure Python 3.6+ is installed on your system

1. Create an AWS user for running the VCFs and attach the admin or readonly role.

1. In `.vscode/launch.json` fill in the `AWS_CLIENT_ID` and `AWS_CLIENT_SECRET` for the VCF user. Or if you have the AWS CLI installed, run `aws configure` and leave the `AWS_CLIENT_ID` and `AWS_CLIENT_SECRET` variables as empty strings. Boto3 will find your default credentials automatically.

1. In `init.sh` (Mac/Linux)/`init.ps1` (Windows) replace YOUR_BITBUCKET_USER with the name of your Cloud Academy BitBucket user

1. Run `init.sh` (Mac/Linux)/`init.ps1` (Windows) to set up the environment

    - Enter your Cloud Academy BitBucket password/[app password](https://confluence.atlassian.com/bitbucket/app-passwords-828781300.html) when prompted.

1. Add the following line to `.gitignore` to avoid committing any sensitive information:

    ```
    .vscode/
    ```

1. Develop and debug functions using the `Current File (Integrated Terminal)` configuration (press F5 with the file open)

## Update Dependencies

1. Run `init.sh` (Mac/Linux)/`init.ps1` (Windows) to set up the virtual environment again. (only the `venv/` directory is impacted by this operation)

## References

- [Boto3 (AWS Python SDK) Reference](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html)
