# Monitoring Notes

This folder contains the files needed to deploy:

- `kube-prometheus-stack` Helm values
- A ServiceMonitor for the FastAPI service
- A PrometheusRule with health and restart alerts
- A Grafana dashboard for CPU, memory, and pod readiness
- Loki values for centralized logging
- Promtail values for shipping cluster logs to Loki

Deploy order:

1. Install the Helm chart with `prometheus-values.yaml`
2. Apply `app-servicemonitor.yaml`
3. Apply `prometheus-rules.yaml`
4. Apply `grafana-dashboard-configmap.yaml`
5. Install Loki with `loki-values.yaml`
6. Install Promtail with `promtail-values.yaml`
