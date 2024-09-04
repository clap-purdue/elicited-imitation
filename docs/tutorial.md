# Tutorial

This is an example tutorial. More will be added.

```python
from gricean_pragmatics import GPMetrics

original_accuracy = 0.85  # 85% accuracy in original context
changed_accuracy = 0.70   # 70% accuracy after subtle contextual changes

# calculate Pragmatic Sensitivity Index (PSI)
psi = GPMetrics.calculate_psi(original_accuracy, changed_accuracy)
print(f"Pragmatic Sensitivity Index (PSI): {psi:.2f}")

```

