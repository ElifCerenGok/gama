import logging
from typing import List, Optional

import pandas as pd

from gama.genetic_programming.components import Individual
from gama.genetic_programming.operator_set import OperatorSet
from gama.search_methods.base_search import (
    BaseSearch,
    _check_base_search_hyperparameters,
)

from dask.distributed import Client, as_completed

log = logging.getLogger(__name__)


class RandomSearch(BaseSearch):
    """ Perform random search over all possible pipelines. """

    def dynamic_defaults(self, x: pd.DataFrame, y: pd.DataFrame, time_limit: float):
        pass

    def search(self, operations: OperatorSet, start_candidates: List[Individual]):
        random_search(operations, self.output, start_candidates)


def random_search(
    operations: OperatorSet,
    output: List[Individual],
    start_candidates: List[Individual],
    max_evaluations: Optional[int] = None,
) -> List[Individual]:
    """ Perform random search over all possible pipelines.

    Parameters
    ----------
    operations: OperatorSet
        An operator set with `evaluate` and `individual` functions.
    output: List[Individual]
        A list which contains the found individuals during search.
    start_candidates: List[Individual]
        A list with candidate individuals to evaluate first.
    max_evaluations: int, optional (default=None)
        If specified, only a maximum of `max_evaluations` individuals are evaluated.
        If None, the algorithm will be run indefinitely.

    Returns
    -------
    List[Individual]
        All evaluated individuals.
    """
    _check_base_search_hyperparameters(operations, output, start_candidates)
    client = Client()
    future_obj = []
    for individual in start_candidates:
        future = client.submit(operations.evaluate, individual)
        future_obj.append(future)
    seq = as_completed(future_obj, with_results=True)
    for futures, result in seq:
        if (max_evaluations is None) or (len(output) < max_evaluations):
            future = futures
            if future is not None:
                output.append(future.result().individual)
            seq.add(client.submit(operations.evaluate, operations.individual()))
        else:
            break

    return output
