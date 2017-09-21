# Space Filling Designs

Python package to download optimal latin hypercube designs

```python
# To get a Latin Hypercube design of 10 points in 3 dimensions optimized with the L2 metric
design = get_maximin_design('lhdl2nd', 10, 3)
```

Designs are downloaded from https://spacefillingdesigns.nl and converted to a python usabled nested list.
