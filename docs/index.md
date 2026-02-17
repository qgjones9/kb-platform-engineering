# Platform Engineering Tools - Categorized by Problem Space

## Container Runtime & Orchestration
- [Docker](container-runtime-and-orchestration/docker/index.md) - Container runtime and platform
- [ContainerD](container-runtime-and-orchestration/containerd/index.md) - Container runtime
- [Crio](container-runtime-and-orchestration/crio/index.md) - Container runtime optimized for Kubernetes
- [Kubernetes](container-runtime-and-orchestration/kubernetes/index.md) - Container orchestration platform

## Service Mesh & Networking
- [Istio](service-mesh-and-networking/istio/index.md) - Service mesh for microservices
- [Cilium](service-mesh-and-networking/cilium/index.md) - Networking, security, and observability using eBPF
- [Envoy](service-mesh-and-networking/envoy/index.md) - Cloud-native edge and service proxy
- [CoreDNS](service-mesh-and-networking/coredns/index.md) - DNS server for Kubernetes
- [Kube-proxy](service-mesh-and-networking/kube-proxy/index.md) - Network proxy for Kubernetes services
- [NGINX](service-mesh-and-networking/nginx/index.md) - Web server, reverse proxy, and load balancer
- [Kiali](observability-and-monitoring/kiali/index.md) - Console for Istio service mesh visualization and troubleshooting

## Security
- [Cert-Manager](security/cert-manager/index.md) - Certificate management for Kubernetes
- [Cosign](security/cosign/index.md) - Sign and verify container images and artifacts (supply chain security)
- [Dependency-Check](security/dependency-check/index.md) - SCA tool that detects publicly disclosed vulnerabilities in project dependencies
- [Fortify](security/fortify/index.md) - Application Security (AppSec) platform for DevSecOps and code security
- [Grype](security/grype/index.md) - Vulnerability scanner for container images and filesystems
- [Kyverno](security/kyverno/index.md) - Policy engine for Kubernetes
- [Syft](security/syft/index.md) - CLI tool for generating Software Bill of Materials (SBOM) from container images and filesystems
- [Trufflehog](security/trufflehog/index.md) - Security scanner for detecting secrets
- [ZAP](security/zap/index.md) - Penetration testing tool for web applications

## Observability & Monitoring
- [Prometheus](observability-and-monitoring/prometheus/index.md) - Monitoring and alerting toolkit
- [Thanos](observability-and-monitoring/thanos/index.md) - Highly available Prometheus setup with long-term storage capabilities
- [Grafana](observability-and-monitoring/grafana/index.md) - Analytics and visualization platform
- [Loki](observability-and-monitoring/grafana/loki/index.md) - Horizontally scalable log aggregation system
- [Promtail](observability-and-monitoring/grafana/promtail/index.md) - Log shipper for Loki
- [Superset](observability-and-monitoring/superset/index.md) - Modern data exploration and data visualization platform
- [Jaeger](observability-and-monitoring/jaeger/index.md) - Distributed tracing system
- [Kubecost](observability-and-monitoring/kubecost/index.md) - Real-time cost visibility and insights for Kubernetes
- [Metrics-server](observability-and-monitoring/metrics-server/index.md) - Resource usage metrics collection for Kubernetes

## CI/CD & GitOps
- [ArgoCD](cicd-and-gitops/argocd/index.md) - GitOps continuous delivery tool for Kubernetes
- [Flux](cicd-and-gitops/flux/index.md) - GitOps tool for keeping Kubernetes clusters in sync with Git repositories
- [Gitlab](cicd-and-gitops/gitlab/index.md) - DevOps platform with CI/CD capabilities
- [Helm](cicd-and-gitops/helm/index.md) - Package manager for Kubernetes
- [Renovate](cicd-and-gitops/renovate/index.md) - Automated dependency updates for multi-platform and multi-language projects
- [SonarQube](cicd-and-gitops/sonarqube/index.md) - Code quality and security analysis tool
- [Cypress](cicd-and-gitops/cypress/index.md) - Front-end E2E testing tool for the modern web

## Platform Engineering & Developer Experience
- [Backstage](platform-engineering-and-developer-experience/backstage/index.md) - Developer portal and platform engineering framework
- [Operator Framework](platform-engineering-and-developer-experience/operator_framework/index.md) - Framework for building Kubernetes operators
- [Platform One]()

## Container Registry
- [Harbor](container-registry/harbor/index.md) - Container image registry with security features

## Authentication & Authorization
- [Keycloak](authentication-and-authorization/keycloak/index.md) - Open-source identity and access management

## Auto-scaling
- [Keda](autoscaling/keda/index.md) - Kubernetes event-driven autoscaling

## Storage & Data
- [etcd](storage-and-data/etcd/index.md) - Distributed key-value store (used by Kubernetes)
- [MinIO](storage-and-data/mini-io/index.md) - High-performance, S3-compatible object storage solution
- [MongoDB](storage-and-data/mongodb/index.md) - Document-oriented NoSQL database
- [Velero](storage-and-data/velero/index.md) - Backup and restore tool for Kubernetes cluster resources and persistent volumes

## API & Communication
- [gRPC](api-and-communication/grpc/index.md) - High-performance RPC framework

