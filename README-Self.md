- install aws cdk

```npm install -g aws-cdk```

- create directory for project

```
mkdir project-1
cd project-1
cdk init app --language=python
cd .venv/Scripts
activate.bat
# Goto project root directory
cd ../../
pip install -r requirements.txt

# Create access keys for iam user from aws console

# aws config
# Enter access key and secret key

cdk synth
cdk ls
cdk deploy
```
One time action per account

``` cdk bootstrap --bootstrap-bucket-name cdk-aviral-bootstrap```

Add below piece of code in app.py only if bootstrap is customized
```
synthesizer=cdk.DefaultStackSynthesizer(
        # synthesizer properties
        file_assets_bucket_name="cdk-aviral-bootstrap"
    )
```

