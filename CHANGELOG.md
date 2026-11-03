# Changelog

## 0.1.0

First release on PyPI.

- `aftershock api-impact`: a library's API change (griffe diff) to the exact consumer lines it breaks, each one verified by
  rules or, with the `model` extra, by a calibrated model; anything uncertain is left for review.
- `aftershock config-contract`, `routes`, `named-queries`: env keys read vs set by a Helm chart, HTTP routes vs URL
  literals in any language, named-query signatures vs payload keys.
- `aftershock pr-check`: one pull request, every applicable lens, one comment.
- Fix proposals and the hold-up ladder (parses, resolves, clears, runs) as a Python API: `aftershock.fix`,
  `aftershock.fixcheck`.
- `aftershock --version`.
- Rules-only install depends on `griffe` alone; the model SDK is the optional `model` extra.
- Benchmarks in `spike/` and their results in `spike/CALIBRATION.md`.
