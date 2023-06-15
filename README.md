# Python Metrics Demo

This repository shows the basics of instrumenting an existing project with Prometheus metrics

- `v1`: is a simple program that subscribes to messages from NATS
- `v2`: the same program exposes metrics (http://localhost:8080/metrics) regarding how many messages have been handled
- `v3`: show how to use labels to have different metrics for each subpath of the subject
- `v4`: introduces an histogram metric regarding the handling duration
- `v5`: uses a custom registry
