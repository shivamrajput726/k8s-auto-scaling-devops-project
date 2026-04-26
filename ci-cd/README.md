# CI/CD Notes

This project uses GitHub Actions for CI/CD.

## Required GitHub Secrets

- `DOCKERHUB_USERNAME`: Your Docker Hub username
- `DOCKERHUB_TOKEN`: Docker Hub access token
- `KUBE_CONFIG_DATA`: Base64-encoded kubeconfig for the target cluster

## Workflow Stages

1. Install Python dependencies
2. Run application tests
3. Build the Docker image
4. Push the Docker image to Docker Hub
5. Render the Kubernetes deployment with the new image tag
6. Deploy to the Kubernetes cluster
7. Wait for the rollout to finish

## Deployment Behavior

- Pull requests run validation without deploying.
- Pushes to `main` and manual workflow runs perform the deployment.
- The image is tagged with both the Git SHA and `latest`.
