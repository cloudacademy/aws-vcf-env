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

## Authentication options

The launch.json encoding of client id, secret, and region for authentication works well for debugging the current file.
To streamline the authentication process when debugging using containers (VS Code Docker debug profile), `aws` default profile credentials and .config.env files are used.
<ins>.config.env is higher precedence</ins> and aws credentials are used as a fallback.

### `aws` CLI credentials

The `aws` CLI credentials can be used by the boto3 Python library to authenticate with AWS.
The `aws` CLI must be authenticated using the default profile (`aws configure`).
The region will be `us-west-2` by default but can be overridden from .config.env.

If `aws` CLI is authenticated a .config.env file can be omitted.

### .config.env file

The .config.env file is similar to the environment variables defined in the launch.json file but is a flat file of variable declarations.
The contents of .config.env resemble:
    
```sh
AWS_CLIENT_ID="AKIA123456789012"
AWS_CLIENT_SECRET="z8lkxhC+2gbDzYAHg7cBcVFEB3a1lhmbBvz3cpIv"
AWS_REGION="us-west-2"
```

As mentioned, `aws` credentials may be used in lieu of `AWS_CLIENT_ID`, and `AWS_CLIENT_SECRET`.
If the AWS_REGION is set in .config.env it overrides the default "us-west-2".

## References

- [Boto3 (AWS Python SDK) Reference](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html)
