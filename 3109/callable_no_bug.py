from typing import Callable, Optional, Union

import abc

class UnweightedAggregationFactory(abc.ABC):
  """Factory for creating `tff.templates.AggregationProcess` without weights."""

  pass


class WeightedAggregationFactory(abc.ABC):
  """Factory for creating `tff.templates.AggregationProcess` with weights."""

  pass 

AggregationFactory = Union[UnweightedAggregationFactory, WeightedAggregationFactory]

def compression_aggregator(
    *,
    zeroing: bool = True,
    clipping: bool = True,
    weighted: bool = True,
    debug_measurements_fn: Optional[Callable[
        [AggregationFactory], AggregationFactory]] = None,
    **kwargs,
) -> AggregationFactory:
    pass

if __name__ == "__main__":
    print("hello world")