# aws-vcf-env

Envrionment for working with AWS VCFs

## Getting started

1. Ensure Python 3.6+ is installed on your system

1. Create an AWS user for running the VCFs and attach the admin or readonly role.

1. In `.vscode/launch.json` fill in the `AWS_CLIENT_ID` and `AWS_CLIENT_SECRET` for the VCF user:

1. Run `init.ps1` to set up the environment

1. Add the following line to `.gitignore` to avoid committing any sensitive information:

    ```
    .vscode/
    ```

1. Develop and debug functions using the `Current File (Integrated Terminal)` configuration (press F5 with the file open)