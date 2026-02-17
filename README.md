# kb-platform-engineering: A Digital Repository for Platform Engineering Knowledge

This repository serves as a centralized, version-controlled environment for documenting platform engineering tools, concepts, and best practices. It is designed to transform static notes into a searchable and collaborative knowledge base, utilizing Markdown for technical documentation and MkDocs for beautiful, accessible documentation sites.

## Core Components and Features

- **Categorized Knowledge Modules**
  The repository is organized by platform engineering domains, such as Container Runtime & Orchestration, Service Mesh & Networking, Observability & Monitoring, CI/CD & GitOps, Security, and more. Each directory contains detailed explanations of tools, their use cases, and practical applications.

- **Tool Documentation**
  A comprehensive collection of platform engineering tools with documentation covering installation, configuration, usage patterns, and integration strategies. By using Git history, users can track how tool configurations and best practices evolve over time.

- **Resource Library and Reference Links**
  Beyond original notes, the repository includes curated external resources, including official documentation, tutorials, and community best practices to provide a comprehensive learning path.

- **Standardized Documentation Format**
  All documentation follows consistent Markdown formatting to ensure clarity and professional presentation across different devices and platforms.

## Knowledge Base Structure

The documentation is organized into the following categories:

### API and Communication

- REST, GraphQL, OpenAPI, WebSocket, Webhooks, gRPC

### Authentication and Authorization

- OAuth, OpenID Connect, JSON Web Token, Basic/Digest/Bearer Authentication, Mutual TLS, Keycloak

### Autoscaling

- Keda (Kubernetes Event-Driven Autoscaling)

### CI/CD and GitOps

- ArgoCD, Flux, GitLab, Helm, Renovate, SonarQube, Cypress

### Container Registry

- Harbor

### Container Runtime and Orchestration

- Docker, containerd, CRI-O

### Observability and Monitoring

- Prometheus, Grafana (with Promtail and Loki), Jaeger, Kiali, Thanos, Kubecost, Superset, Metrics Server

### Platform Engineering and Developer Experience

- Backstage, Platform One, Operator Framework

### Security

- Kyverno, Cosign, Fortify

### Service Mesh and Networking

- Istio, Envoy, Cilium, CoreDNS, kube-proxy, NGINX

### Storage and Data

- Velero, etcd, MongoDB, MinIO

## Using MkDocs to View Documentation

### Getting Started with MkDocs

Content below is from the [MkDocs Installation guide](https://www.mkdocs.org/user-guide/installation/).

---

## MkDocs Installation

A detailed guide.

### Requirements

MkDocs requires a recent version of [Python](https://www.python.org/) and the Python package manager, [pip](https://pip.readthedocs.io/en/stable/installing/), to be installed on your system.

You can check if you already have these installed from the command line:

```console
$ python --version
Python 3.8.2
$ pip --version
pip 20.0.2 from /usr/local/lib/python3.8/site-packages/pip (python 3.8)
```

If you already have those packages installed, you may skip down to [Installing MkDocs](#installing-mkdocs).

### Installing Python

Install [Python](https://www.python.org/) using your package manager of choice, or by downloading an installer appropriate for your system from [python.org](https://www.python.org/downloads/) and running it.

> **Note:** If you are installing Python on Windows, be sure to check the box to have Python added to your PATH if the installer offers such an option (it's normally off by default). _Add Python to PATH_

### Installing pip

If you're using a recent version of Python, the Python package manager, [pip](https://pip.readthedocs.io/en/stable/installing/), is most likely installed by default. However, you may need to upgrade pip to the latest version:

```bash
pip install --upgrade pip
```

If you need to install pip for the first time, download [get-pip.py](https://bootstrap.pypa.io/get-pip.py). Then run the following command to install it:

```bash
python get-pip.py
```

## Installing MkDocs

Install the `mkdocs` package using pip:

```bash
pip install mkdocs
```

You should now have the `mkdocs` command installed on your system. Run `mkdocs --version` to check that everything worked okay.

```console
$ mkdocs --version
mkdocs, version 1.2.0 from /usr/local/lib/python3.8/site-packages/mkdocs (Python 3.8)
```

> **Note:** If you would like manpages installed for MkDocs, the [click-man](https://github.com/click-contrib/click-man) tool can generate and install them for you. Simply run the following two commands:
>
> ```bash
> pip install click-man
> click-man --target path/to/man/pages mkdocs
> ```
>
> See the [click-man documentation](https://github.com/click-contrib/click-man#automatic-man-page-installation-with-setuptools-and-pip) for an explanation of why manpages are not automatically generated and installed by pip.

> **Note:** If you are using Windows, some of the above commands may not work out-of-the-box. A quick solution may be to preface every Python command with `python -m` like this:
>
> ```bash
> python -m pip install mkdocs
> python -m mkdocs
> ```
>
> For a more permanent solution, you may need to edit your `PATH` environment variable to include the `Scripts` directory of your Python installation. Recent versions of Python include a script to do this for you. Navigate to your Python installation directory (for example `C:\Python38\`), open the `Tools`, then `Scripts` folder, and run the `win_add2path.py` file by double clicking on it. Alternatively, you can download the [script](https://github.com/python/cpython/blob/master/Tools/scripts/win_add2path.py) and run it (`python win_add2path.py`).

## Running the Documentation Site

Once MkDocs is installed, you can serve the documentation locally:

```bash
mkdocs serve
```

This will start a local development server at `http://127.0.0.1:8000` where you can view the documentation in your browser.

To build the documentation site:

```bash
mkdocs build
```

This creates a `site` directory containing the static HTML files for the documentation.

---
