# Temporal Hello World in Python

A basic "Hello World" Temporal application with environment-based 
configuration that provides support for a local Temporal Service
or Temporal Cloud.

## Features

- Well-structured Workflow and Activity code in Python
- Dynamic Workflow logic that selects an Activity based on input data
- Can switch between local Temporal Service and Temporal Cloud without modifying code
- Supports both mTLS and API Key authentication


## Running the Example With a Local Temporal Service

The application is configured to use a local Temporal Service by 
default, so you don't need to set any environment variables in
this case. Open a new terminal window and run the following command
to start the Temporal Service:

```
temporal server start-dev
```

1. Create a virtual environment and activate it. On macOS and Linux, 
   run these commands:

   ```
   python3 -m venv env
   source env/bin/activate
   ```

   On Windows, run these commands:
   ```
   python3 -m venv env
   env\Scripts\activate
   ```

2. Install the Temporal SDK within this virtual environment:

   ```
   python3 -m pip install temporalio
   ```

3. Run the Worker:

   ```bash
   python3 run_worker.py
   ```

4. Open another terminal window and activate the virtual environment.
   On macOS or Linux, run this command:

   ```
   source env/bin/activate
   ```

   On Windows, run this command:

   ```
   env\Scripts\activate
   ```

5. Start the Workflow and supply a name as input:

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



## Running the example with Temporal Cloud

You can use Temporal Cloud instead of running a local Temporal Service.
To do so, you need only set some combination of the five environment
variables below to specify how the application should connect to and 
authenticate with Temporal Cloud.


| Variable Name          | Example                               | Description
|------------------------|---------------------------------------|-------------------
| `TEMPORAL_ADDRESS`     | `us-east-1.aws.api.temporal.io:7233`  | Temporal Service endpoint address (hostname:port) 
| `TEMPORAL_NAMESPACE`   | `example.c9ef8`                       | Name of the Namespace within Temporal Cloud
| `TEMPORAL_API_KEY`     | `abc123.actual.value.redacted.xyz789` | API Key for Temporal Cloud authentication
| `TEMPORAL_TLS_CERT`    | `/path/to/client.pem`                 | Path to TLS client certificate file
| `TEMPORAL_TLS_KEY`     | `/path/to/client.key`                 | Path to TLS private key file


If you are using API Key authentication, which we recommend, you must
set only the first three variables in the table above. Alternatively, 
you can use mTLS authentication, in which case you must set only the
first two and last two. The next two sections provide examples of this.

IMPORTANT: You must set these environment variables in both terminal
windows (i.e., the one where you launch the Worker and the one where
you start the Workflow).

Once you have set these environment variables, you can repeat steps
1-5 in the "Running the example with a local Temporal Service" above.

### Use Temporal Cloud with API Key authentication

In the commands below, replace the quoted values with the ones
for [your Temporal Cloud Namespace](https://docs.temporal.io/cloud/namespaces#access-namespaces). If you're using Microsoft Windows, you may need to
replace `export` with `set`.


```bash
export TEMPORAL_ADDRESS="region.cloud.api.temporal.io:7233"
export TEMPORAL_NAMESPACE="example.c9ef8"
export TEMPORAL_API_KEY="abc123.actual.value.redacted.xyz789"
```

### Use Temporal Cloud with mTLS authentication

In the commands below, replace the quoted values with the ones
for [your Temporal Cloud Namespace](https://docs.temporal.io/cloud/namespaces#access-namespaces). If you're using Microsoft Windows, you may need to
replace `export` with `set`.


```bash
export TEMPORAL_ADDRESS="your-namespace.tmprl.cloud:7233"
export TEMPORAL_NAMESPACE="example.c9ef8"
export TEMPORAL_TLS_CERT="/path/to/client.pem"
export TEMPORAL_TLS_KEY="/path/to/client.key"
```

## Project structure

- `workflows.py` - Code that defines the Workflow
- `activities.py` - Code that defines the Activities
- `run_worker.py` - Code used to configure and launch the Worker
- `start_workflow.py` - Code that requests execution of the Workflow and displays the result
- `client_provider.py` - Code that configures the Temporal Client based on environment variables


