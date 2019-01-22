import logging
import uuid

import numpy

from dagster import (
    DependencyDefinition,
    ExecutionContext,
    InputDefinition,
    lambda_solid,
    PipelineContextDefinition,
    PipelineDefinition,
    ReentrantInfo,
)
from dagster.utils import load_yaml_from_path, script_relative_path
from dagma.execution import execute_pipeline


def create_lambda_context():
    return PipelineContextDefinition(
        context_fn=lambda info: ExecutionContext.console_logging(log_level=logging.DEBUG)
    )


@lambda_solid
def solid_a():
    return 1


@lambda_solid(inputs=[InputDefinition('arg_a')])
def solid_b(arg_a):
    return arg_a * 2


@lambda_solid(inputs=[InputDefinition('arg_a')])
def solid_c(arg_a):
    return arg_a * 3


@lambda_solid(inputs=[InputDefinition('arg_b'), InputDefinition('arg_c')])
def solid_d(arg_b, arg_c):
    return arg_b + arg_c / 2.0


@lambda_solid
def solid_e():
    return numpy.mean([1, 2, 3])
    # TODO: figure out how to deal with installing packages like numpy where the target
    # architecture on lambda is not the architecture running the pipeline
    # Maybe build remotely


def define_diamond_dag_pipeline():
    return PipelineDefinition(
        name='actual_dag_pipeline',
        solids=[solid_a, solid_b, solid_c, solid_d],
        dependencies={
            'solid_b': {'arg_a': DependencyDefinition('solid_a')},
            'solid_c': {'arg_a': DependencyDefinition('solid_a')},
            'solid_d': {
                'arg_b': DependencyDefinition('solid_b'),
                'arg_c': DependencyDefinition('solid_c'),
            },
        },
    )


def define_single_solid_pipeline():
    return PipelineDefinition(name='single_solid_pipeline', solids=[solid_a], dependencies={})


def define_numpy_pipeline():
    return PipelineDefinition(name='numpy_pipeline', solids=[solid_e], dependencies={})


NULL_PIPELINE = PipelineDefinition([])


def run_test_pipeline(pipeline):
    return execute_pipeline(
        pipeline=pipeline,
        environment={},
        dagma_config=load_yaml_from_path(script_relative_path('dagma_config.yml')),
        additional_includes=[],
        additional_requirements=[],
        root_directory=script_relative_path('.'),
    )


# def test_execution_diamond():
#     pipeline = define_diamond_dag_pipeline()
#     results = run_test_pipeline(pipeline)

#     assert len(results) == 4


def test_execution_null():
    pipeline = NULL_PIPELINE
    results = list(run_test_pipeline(pipeline))

    assert not results


def test_execution_single():
    pipeline = define_single_solid_pipeline()
    results = list(run_test_pipeline(pipeline))

    assert len(results) == 1
    assert results[('solid_a.transform', 'result')][0] is True
    assert results[('solid_a.transform', 'result')][1].output_name == 'result'
    assert results[('solid_a.transform', 'result')][1].value == 1
    assert results[('solid_a.transform', 'result')][2] is None


# def test_execution_numpy():
#     pipeline = define_numpy_pipeline()
#     results = run_test_pipeline(pipeline)

#     assert len(results) == 1
#     assert results[('solid_a.transform', 'result')][0] is True
#     assert results[('solid_a.transform', 'result')][1].output_name == 'result'
#     assert results[('solid_a.transform', 'result')][1].value == 2.0
#     assert results[('solid_a.transform', 'result')][2] is None
