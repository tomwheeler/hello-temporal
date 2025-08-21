# Hello World (Python Version)

Clone this repository and change into this directory.

```bash
git clone https://github.com/temporalio/hello-temporal
cd hello-temporal
cd python
```

This example has been tested with Python 3.13, but should work
with any recent version of Python.

## Prerequisite steps for running the example

This example can use either a self-hosted Temporal Service or
Temporal Cloud. The application is designed to configure itself
based on environment variables, so you can switch between these
without changing a single line of code. 

### Complete these steps before running the example locally

You can run this example locally by using the `temporal` CLI
to start the Temporal Service on your machine. If you have not
already installed the `temporal` CLI, follow the steps listed in
the [Install the Temporal CLI](https://docs.temporal.io/cli#install)
documentation.

The application is configured to use a local Temporal Service by 
default, so you don't need to set any environment variables in
this case, but the service must be running. Open a new terminal 
window and run the following command to start it:

```
temporal server start-dev
```

### Complete these steps before running the example with Temporal Cloud

If you have a Temporal Cloud account, you can use Temporal Cloud
instead of running a local Temporal Service as described in the 
previous section. To do this, you must set three environment variables
in both of the terminal windows where you run the code.

| Variable Name          | Example                               | Description
|------------------------|---------------------------------------|-------------------
| `TEMPORAL_ADDRESS`     | `us-east-1.aws.api.temporal.io:7233`  | Temporal Service endpoint address (hostname:port) 
| `TEMPORAL_NAMESPACE`   | `example.c9ef8`                       | Name of the Namespace within Temporal Cloud
| `TEMPORAL_API_KEY`     | `abc123.actual.value.redacted.xyz789` | API Key for Temporal Cloud authentication


As an alternative to API Key authentication, you can use mTLS authentication
with either Temporal Cloud or a self-hosted Temporal Service that's configured
to support mTLS. To do this, do not set the `TEMPORAL_API_KEY` environment
variable. Instead, set the `TEMPORAL_TLS_CERT` and `TEMPORAL_TLS_KEY`
environment variables to the path of your certificate and private key file,
respectively.


## Running the application

Create a virtual environment and activate it. On macOS and Linux, run 
these commands:

```
python3 -m venv env
source env/bin/activate
```

On Windows, run these commands:

```
python3 -m venv env
env\Scripts\activate
```

Now, install the Temporal SDK within this virtual environment:

```
python3 -m pip install temporalio
```



Next, run the Worker:


```bash
python3 run_worker.py
```


In another window, activate the virtual environment:

On macOS or Linux, run this command:

```
source env/bin/activate
```

On Windows, run this command:

```
env\Scripts\activate
```

Finally, start the Workflow, supplying a name as its input:

```bash
python3 start_workflow.py Ted
```

You should then see its output, a greeting customized with the
specified name, displayed to your terminal. 

If you repeat this step using different names as input, you may
observe that the greeting is in Spanish or Turkish instead of
English. That's because this particular Workflow uses Activities
to generate the greeting in a given language and it decides which
one to call based on the length of the name supplied as input.
Temporal Workflows support dynamic logic. Not only can they decide
what to do based on the data passed as input, they can also decide
what to do based on the result returned by an Activity called as
the Workflow runs.
