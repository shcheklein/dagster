# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_scaffold_airflow_dag 1'] = [
    "'''Static scaffolding autogenerated by dagster-airflow from pipeline demo_pipeline with config:",
    '',
    '    context:',
    '      default:',
    '        config: {log_level: DEBUG}',
    '    solids:',
    '      multiply_the_word:',
    '        config: {factor: 2}',
    '        inputs:',
    '          word: {value: bar}',
    '    ',
    '',
    'By convention, users should attempt to isolate post-codegen changes and customizations to the',
    '"editable" demo_pipeline_editable__scaffold.py file, rather than changing the definitions in this',
    '"static" file. Please let us know if you are encountering use cases where it is necessary to make',
    'changes to the static file.',
    "'''",
    '',
    'from airflow import DAG',
    'from airflow.operators.dagster_plugin import DagsterOperator',
    '',
    '',
    "CONFIG = '''",
    '    {',
    '      context: {',
    '        default: {',
    '          config: {',
    '            log_level: "DEBUG"',
    '          }',
    '        }',
    '      },',
    '      solids: {',
    '        multiply_the_word: {',
    '          config: {',
    '            factor: 2',
    '          },',
    '          inputs: {',
    '            word: {',
    '              value: "bar"',
    '            }',
    '          }',
    '        }',
    '      }',
    '    }',
    "'''",
    '',
    '',
    'def make_dag(',
    '    dag_id,',
    '    dag_description,',
    '    dag_kwargs,',
    '    s3_conn_id,',
    '    modified_docker_operator_kwargs,',
    '    host_tmp_dir',
    '):',
    '    dag = DAG(',
    '        dag_id=dag_id,',
    '        description=dag_description,',
    '        **dag_kwargs,',
    '    )',
    '',
    '    multiply__the__word_word_input__thunk_task = DagsterOperator(',
    "        step='multiply_the_word.word.input_thunk',",
    '        config=CONFIG,',
    '        dag=dag,',
    "        tmp_dir='/tmp/results',",
    '        host_tmp_dir=host_tmp_dir,',
    "        image='dagster-airflow-demo',",
    "        task_id='multiply__the__word_word_input__thunk',",
    '        s3_conn_id=s3_conn_id,',
    "        command='''-q '",
    '            mutation {{',
    '              startSubplanExecution(',
    '                config: {config},',
    '                executionMetadata: {{',
    '                  runId: "testRun"',
    '                }},',
    '                pipelineName: "demo_pipeline",',
    '                stepExecutions: [',
    '                  {{',
    '                    stepKey: "multiply_the_word.word.input_thunk"',
    '                  }}',
    '                ],',
    '                marshalledInputs: ',
    '                [',
    '                ],',
    '                marshalledOutputs: ',
    '                [',
    '                  {{',
    '                    outputName: "input_thunk_output",',
    '                    key: "/tmp/results/multiply__the__word_word_input__thunk___input__thunk__output.pickle"',
    '                  }}',
    '                ],',
    '              ) {{',
    '                __typename',
    '              }}',
    "            '",
    "        '''.format(config=CONFIG),",
    '    )',
    '',
    '    multiply__the__word_transform_task = DagsterOperator(',
    "        step='multiply_the_word.transform',",
    '        config=CONFIG,',
    '        dag=dag,',
    "        tmp_dir='/tmp/results',",
    '        host_tmp_dir=host_tmp_dir,',
    "        image='dagster-airflow-demo',",
    "        task_id='multiply__the__word_transform',",
    '        s3_conn_id=s3_conn_id,',
    "        command='''-q '",
    '            mutation {{',
    '              startSubplanExecution(',
    '                config: {config},',
    '                executionMetadata: {{',
    '                  runId: "testRun"',
    '                }},',
    '                pipelineName: "demo_pipeline",',
    '                stepExecutions: [',
    '                  {{',
    '                    stepKey: "multiply_the_word.transform"',
    '                  }}',
    '                ],',
    '                marshalledInputs: ',
    '                [',
    '                  {{',
    '                    inputName: "word",',
    '                    key: "/tmp/results/multiply__the__word_word_input__thunk___input__thunk__output.pickle"',
    '                  }}',
    '                ],',
    '                marshalledOutputs: ',
    '                [',
    '                  {{',
    '                    outputName: "result",',
    '                    key: "/tmp/results/multiply__the__word_transform___result.pickle"',
    '                  }}',
    '                ],',
    '              ) {{',
    '                __typename',
    '              }}',
    "            '",
    "        '''.format(config=CONFIG),",
    '    )',
    '',
    '    count__letters_transform_task = DagsterOperator(',
    "        step='count_letters.transform',",
    '        config=CONFIG,',
    '        dag=dag,',
    "        tmp_dir='/tmp/results',",
    '        host_tmp_dir=host_tmp_dir,',
    "        image='dagster-airflow-demo',",
    "        task_id='count__letters_transform',",
    '        s3_conn_id=s3_conn_id,',
    "        command='''-q '",
    '            mutation {{',
    '              startSubplanExecution(',
    '                config: {config},',
    '                executionMetadata: {{',
    '                  runId: "testRun"',
    '                }},',
    '                pipelineName: "demo_pipeline",',
    '                stepExecutions: [',
    '                  {{',
    '                    stepKey: "count_letters.transform"',
    '                  }}',
    '                ],',
    '                marshalledInputs: ',
    '                [',
    '                  {{',
    '                    inputName: "word",',
    '                    key: "/tmp/results/multiply__the__word_transform___result.pickle"',
    '                  }}',
    '                ],',
    '                marshalledOutputs: ',
    '                [',
    '                  {{',
    '                    outputName: "result",',
    '                    key: "/tmp/results/count__letters_transform___result.pickle"',
    '                  }}',
    '                ],',
    '              ) {{',
    '                __typename',
    '              }}',
    "            '",
    "        '''.format(config=CONFIG),",
    '    )',
    '',
    '    multiply__the__word_word_input__thunk_task.set_downstream(multiply__the__word_transform_task)',
    '    multiply__the__word_transform_task.set_downstream(count__letters_transform_task)',
    '',
    '    return dag',
    ''
]

snapshots['test_scaffold_airflow_dag 2'] = [
    "'''Editable scaffolding autogenerated by dagster-airflow from pipeline demo_pipeline with config:",
    '',
    '    context:',
    '      default:',
    '        config: {log_level: DEBUG}',
    '    solids:',
    '      multiply_the_word:',
    '        config: {factor: 2}',
    '        inputs:',
    '          word: {value: bar}',
    '    ',
    '',
    'By convention, users should attempt to isolate post-codegen changes and customizations to this',
    '"editable" file, rather than changing the definitions in the "static"',
    'demo_pipeline_static__scaffold.py file. Please let us know if you are encountering use cases where',
    'it is necessary to make changes to the static file.',
    "'''",
    '',
    'import datetime',
    '',
    'from demo_pipeline_static__scaffold import make_dag',
    '',
    '# Arguments to be passed to the ``default_args`` parameter of the ``airflow.DAG`` constructor.You',
    '# can override these with values of your choice.',
    'DEFAULT_ARGS = {',
    "    'depends_on_past': False,",
    "    'email': ['airflow@example.com'],",
    "    'email_on_failure': False,",
    "    'email_on_retry': False,",
    "    'owner': 'airflow',",
    "    'retries': 1,",
    "    'retry_delay': datetime.timedelta(0, 300),",
    '}',
    '',
    '# Any additional keyword arguments to be passed to the ``airflow.DAG`` constructor. You can override',
    '# these with values of your choice.',
    'DAG_KWARGS = {}',
    '',
    '# The name of the autogenerated DAG. By default, this is just the name of the Dagster pipeline from',
    '# which the Airflow DAG was generated (demo_pipeline). You may want to override this if, for',
    '# instance, you want to schedule multiple DAGs corresponding to different configurations of the same',
    '# Dagster pipeline.',
    "DAG_ID = 'demo_pipeline'",
    '',
    '# The description of the autogenerated DAG. By default, this is the description of the Dagster',
    '# pipeline from which the Airflow DAG was generated. You may want to override this, as with the',
    '# DAG_ID parameter.',
    "DAG_DESCRIPTION = '''***Autogenerated by dagster-airflow***'''",
    '',
    '# Additional arguments, if any, to pass to the underlying',
    '# ``dagster_airflow.dagster_plugin.ModifiedDockerOperator`` constructor. Set these if, for instance,',
    '# you need to set special TLS parameters.',
    'MODIFIED_DOCKER_OPERATOR_KWARGS = {}',
    '',
    '# Set your S3 connection id here, if you do not want to use the default ``aws_default`` connection.',
    "S3_CONN_ID = 'aws_default'",
    '',
    '# Set the host directory to mount into /tmp/results on the containers.',
    "HOST_TMP_DIR = '/tmp/results'",
    '',
    'dag = make_dag(',
    '    dag_id=DAG_ID,',
    '    dag_description=DAG_DESCRIPTION,',
    '    dag_kwargs=dict(default_args=DEFAULT_ARGS, **DAG_KWARGS),',
    '    s3_conn_id=S3_CONN_ID,',
    '    modified_docker_operator_kwargs=MODIFIED_DOCKER_OPERATOR_KWARGS,',
    '    host_tmp_dir=HOST_TMP_DIR,',
    ')',
    ''
]

snapshots['test_scaffold_airflow_dag_specify_dir 1'] = [
    "'''Static scaffolding autogenerated by dagster-airflow from pipeline demo_pipeline with config:",
    '',
    '    context:',
    '      default:',
    '        config: {log_level: DEBUG}',
    '    solids:',
    '      multiply_the_word:',
    '        config: {factor: 2}',
    '        inputs:',
    '          word: {value: bar}',
    '    ',
    '',
    'By convention, users should attempt to isolate post-codegen changes and customizations to the',
    '"editable" demo_pipeline_editable__scaffold.py file, rather than changing the definitions in this',
    '"static" file. Please let us know if you are encountering use cases where it is necessary to make',
    'changes to the static file.',
    "'''",
    '',
    'from airflow import DAG',
    'from airflow.operators.dagster_plugin import DagsterOperator',
    '',
    '',
    "CONFIG = '''",
    '    {',
    '      context: {',
    '        default: {',
    '          config: {',
    '            log_level: "DEBUG"',
    '          }',
    '        }',
    '      },',
    '      solids: {',
    '        multiply_the_word: {',
    '          config: {',
    '            factor: 2',
    '          },',
    '          inputs: {',
    '            word: {',
    '              value: "bar"',
    '            }',
    '          }',
    '        }',
    '      }',
    '    }',
    "'''",
    '',
    '',
    'def make_dag(',
    '    dag_id,',
    '    dag_description,',
    '    dag_kwargs,',
    '    s3_conn_id,',
    '    modified_docker_operator_kwargs,',
    '    host_tmp_dir',
    '):',
    '    dag = DAG(',
    '        dag_id=dag_id,',
    '        description=dag_description,',
    '        **dag_kwargs,',
    '    )',
    '',
    '    multiply__the__word_word_input__thunk_task = DagsterOperator(',
    "        step='multiply_the_word.word.input_thunk',",
    '        config=CONFIG,',
    '        dag=dag,',
    "        tmp_dir='/tmp/results',",
    '        host_tmp_dir=host_tmp_dir,',
    "        image='dagster-airflow-demo',",
    "        task_id='multiply__the__word_word_input__thunk',",
    '        s3_conn_id=s3_conn_id,',
    "        command='''-q '",
    '            mutation {{',
    '              startSubplanExecution(',
    '                config: {config},',
    '                executionMetadata: {{',
    '                  runId: "testRun"',
    '                }},',
    '                pipelineName: "demo_pipeline",',
    '                stepExecutions: [',
    '                  {{',
    '                    stepKey: "multiply_the_word.word.input_thunk"',
    '                  }}',
    '                ],',
    '                marshalledInputs: ',
    '                [',
    '                ],',
    '                marshalledOutputs: ',
    '                [',
    '                  {{',
    '                    outputName: "input_thunk_output",',
    '                    key: "/tmp/results/multiply__the__word_word_input__thunk___input__thunk__output.pickle"',
    '                  }}',
    '                ],',
    '              ) {{',
    '                __typename',
    '              }}',
    "            '",
    "        '''.format(config=CONFIG),",
    '    )',
    '',
    '    multiply__the__word_transform_task = DagsterOperator(',
    "        step='multiply_the_word.transform',",
    '        config=CONFIG,',
    '        dag=dag,',
    "        tmp_dir='/tmp/results',",
    '        host_tmp_dir=host_tmp_dir,',
    "        image='dagster-airflow-demo',",
    "        task_id='multiply__the__word_transform',",
    '        s3_conn_id=s3_conn_id,',
    "        command='''-q '",
    '            mutation {{',
    '              startSubplanExecution(',
    '                config: {config},',
    '                executionMetadata: {{',
    '                  runId: "testRun"',
    '                }},',
    '                pipelineName: "demo_pipeline",',
    '                stepExecutions: [',
    '                  {{',
    '                    stepKey: "multiply_the_word.transform"',
    '                  }}',
    '                ],',
    '                marshalledInputs: ',
    '                [',
    '                  {{',
    '                    inputName: "word",',
    '                    key: "/tmp/results/multiply__the__word_word_input__thunk___input__thunk__output.pickle"',
    '                  }}',
    '                ],',
    '                marshalledOutputs: ',
    '                [',
    '                  {{',
    '                    outputName: "result",',
    '                    key: "/tmp/results/multiply__the__word_transform___result.pickle"',
    '                  }}',
    '                ],',
    '              ) {{',
    '                __typename',
    '              }}',
    "            '",
    "        '''.format(config=CONFIG),",
    '    )',
    '',
    '    count__letters_transform_task = DagsterOperator(',
    "        step='count_letters.transform',",
    '        config=CONFIG,',
    '        dag=dag,',
    "        tmp_dir='/tmp/results',",
    '        host_tmp_dir=host_tmp_dir,',
    "        image='dagster-airflow-demo',",
    "        task_id='count__letters_transform',",
    '        s3_conn_id=s3_conn_id,',
    "        command='''-q '",
    '            mutation {{',
    '              startSubplanExecution(',
    '                config: {config},',
    '                executionMetadata: {{',
    '                  runId: "testRun"',
    '                }},',
    '                pipelineName: "demo_pipeline",',
    '                stepExecutions: [',
    '                  {{',
    '                    stepKey: "count_letters.transform"',
    '                  }}',
    '                ],',
    '                marshalledInputs: ',
    '                [',
    '                  {{',
    '                    inputName: "word",',
    '                    key: "/tmp/results/multiply__the__word_transform___result.pickle"',
    '                  }}',
    '                ],',
    '                marshalledOutputs: ',
    '                [',
    '                  {{',
    '                    outputName: "result",',
    '                    key: "/tmp/results/count__letters_transform___result.pickle"',
    '                  }}',
    '                ],',
    '              ) {{',
    '                __typename',
    '              }}',
    "            '",
    "        '''.format(config=CONFIG),",
    '    )',
    '',
    '    multiply__the__word_word_input__thunk_task.set_downstream(multiply__the__word_transform_task)',
    '    multiply__the__word_transform_task.set_downstream(count__letters_transform_task)',
    '',
    '    return dag',
    ''
]

snapshots['test_scaffold_airflow_dag_specify_dir 2'] = [
    "'''Editable scaffolding autogenerated by dagster-airflow from pipeline demo_pipeline with config:",
    '',
    '    context:',
    '      default:',
    '        config: {log_level: DEBUG}',
    '    solids:',
    '      multiply_the_word:',
    '        config: {factor: 2}',
    '        inputs:',
    '          word: {value: bar}',
    '    ',
    '',
    'By convention, users should attempt to isolate post-codegen changes and customizations to this',
    '"editable" file, rather than changing the definitions in the "static"',
    'demo_pipeline_static__scaffold.py file. Please let us know if you are encountering use cases where',
    'it is necessary to make changes to the static file.',
    "'''",
    '',
    'import datetime',
    '',
    'from demo_pipeline_static__scaffold import make_dag',
    '',
    '# Arguments to be passed to the ``default_args`` parameter of the ``airflow.DAG`` constructor.You',
    '# can override these with values of your choice.',
    'DEFAULT_ARGS = {',
    "    'depends_on_past': False,",
    "    'email': ['airflow@example.com'],",
    "    'email_on_failure': False,",
    "    'email_on_retry': False,",
    "    'owner': 'airflow',",
    "    'retries': 1,",
    "    'retry_delay': datetime.timedelta(0, 300),",
    '}',
    '',
    '# Any additional keyword arguments to be passed to the ``airflow.DAG`` constructor. You can override',
    '# these with values of your choice.',
    'DAG_KWARGS = {}',
    '',
    '# The name of the autogenerated DAG. By default, this is just the name of the Dagster pipeline from',
    '# which the Airflow DAG was generated (demo_pipeline). You may want to override this if, for',
    '# instance, you want to schedule multiple DAGs corresponding to different configurations of the same',
    '# Dagster pipeline.',
    "DAG_ID = 'demo_pipeline'",
    '',
    '# The description of the autogenerated DAG. By default, this is the description of the Dagster',
    '# pipeline from which the Airflow DAG was generated. You may want to override this, as with the',
    '# DAG_ID parameter.',
    "DAG_DESCRIPTION = '''***Autogenerated by dagster-airflow***'''",
    '',
    '# Additional arguments, if any, to pass to the underlying',
    '# ``dagster_airflow.dagster_plugin.ModifiedDockerOperator`` constructor. Set these if, for instance,',
    '# you need to set special TLS parameters.',
    'MODIFIED_DOCKER_OPERATOR_KWARGS = {}',
    '',
    '# Set your S3 connection id here, if you do not want to use the default ``aws_default`` connection.',
    "S3_CONN_ID = 'aws_default'",
    '',
    '# Set the host directory to mount into /tmp/results on the containers.',
    "HOST_TMP_DIR = '/tmp/results'",
    '',
    'dag = make_dag(',
    '    dag_id=DAG_ID,',
    '    dag_description=DAG_DESCRIPTION,',
    '    dag_kwargs=dict(default_args=DEFAULT_ARGS, **DAG_KWARGS),',
    '    s3_conn_id=S3_CONN_ID,',
    '    modified_docker_operator_kwargs=MODIFIED_DOCKER_OPERATOR_KWARGS,',
    '    host_tmp_dir=HOST_TMP_DIR,',
    ')',
    ''
]

snapshots['test_scaffold_airflow_dag_specify_paths 1'] = [
    "'''Static scaffolding autogenerated by dagster-airflow from pipeline demo_pipeline with config:",
    '',
    '    context:',
    '      default:',
    '        config: {log_level: DEBUG}',
    '    solids:',
    '      multiply_the_word:',
    '        config: {factor: 2}',
    '        inputs:',
    '          word: {value: bar}',
    '    ',
    '',
    'By convention, users should attempt to isolate post-codegen changes and customizations to the',
    '"editable" bar.py file, rather than changing the definitions in this "static" file. Please let us',
    'know if you are encountering use cases where it is necessary to make changes to the static file.',
    "'''",
    '',
    'from airflow import DAG',
    'from airflow.operators.dagster_plugin import DagsterOperator',
    '',
    '',
    "CONFIG = '''",
    '    {',
    '      context: {',
    '        default: {',
    '          config: {',
    '            log_level: "DEBUG"',
    '          }',
    '        }',
    '      },',
    '      solids: {',
    '        multiply_the_word: {',
    '          config: {',
    '            factor: 2',
    '          },',
    '          inputs: {',
    '            word: {',
    '              value: "bar"',
    '            }',
    '          }',
    '        }',
    '      }',
    '    }',
    "'''",
    '',
    '',
    'def make_dag(',
    '    dag_id,',
    '    dag_description,',
    '    dag_kwargs,',
    '    s3_conn_id,',
    '    modified_docker_operator_kwargs,',
    '    host_tmp_dir',
    '):',
    '    dag = DAG(',
    '        dag_id=dag_id,',
    '        description=dag_description,',
    '        **dag_kwargs,',
    '    )',
    '',
    '    multiply__the__word_word_input__thunk_task = DagsterOperator(',
    "        step='multiply_the_word.word.input_thunk',",
    '        config=CONFIG,',
    '        dag=dag,',
    "        tmp_dir='/tmp/results',",
    '        host_tmp_dir=host_tmp_dir,',
    "        image='dagster-airflow-demo',",
    "        task_id='multiply__the__word_word_input__thunk',",
    '        s3_conn_id=s3_conn_id,',
    "        command='''-q '",
    '            mutation {{',
    '              startSubplanExecution(',
    '                config: {config},',
    '                executionMetadata: {{',
    '                  runId: "testRun"',
    '                }},',
    '                pipelineName: "demo_pipeline",',
    '                stepExecutions: [',
    '                  {{',
    '                    stepKey: "multiply_the_word.word.input_thunk"',
    '                  }}',
    '                ],',
    '                marshalledInputs: ',
    '                [',
    '                ],',
    '                marshalledOutputs: ',
    '                [',
    '                  {{',
    '                    outputName: "input_thunk_output",',
    '                    key: "/tmp/results/multiply__the__word_word_input__thunk___input__thunk__output.pickle"',
    '                  }}',
    '                ],',
    '              ) {{',
    '                __typename',
    '              }}',
    "            '",
    "        '''.format(config=CONFIG),",
    '    )',
    '',
    '    multiply__the__word_transform_task = DagsterOperator(',
    "        step='multiply_the_word.transform',",
    '        config=CONFIG,',
    '        dag=dag,',
    "        tmp_dir='/tmp/results',",
    '        host_tmp_dir=host_tmp_dir,',
    "        image='dagster-airflow-demo',",
    "        task_id='multiply__the__word_transform',",
    '        s3_conn_id=s3_conn_id,',
    "        command='''-q '",
    '            mutation {{',
    '              startSubplanExecution(',
    '                config: {config},',
    '                executionMetadata: {{',
    '                  runId: "testRun"',
    '                }},',
    '                pipelineName: "demo_pipeline",',
    '                stepExecutions: [',
    '                  {{',
    '                    stepKey: "multiply_the_word.transform"',
    '                  }}',
    '                ],',
    '                marshalledInputs: ',
    '                [',
    '                  {{',
    '                    inputName: "word",',
    '                    key: "/tmp/results/multiply__the__word_word_input__thunk___input__thunk__output.pickle"',
    '                  }}',
    '                ],',
    '                marshalledOutputs: ',
    '                [',
    '                  {{',
    '                    outputName: "result",',
    '                    key: "/tmp/results/multiply__the__word_transform___result.pickle"',
    '                  }}',
    '                ],',
    '              ) {{',
    '                __typename',
    '              }}',
    "            '",
    "        '''.format(config=CONFIG),",
    '    )',
    '',
    '    count__letters_transform_task = DagsterOperator(',
    "        step='count_letters.transform',",
    '        config=CONFIG,',
    '        dag=dag,',
    "        tmp_dir='/tmp/results',",
    '        host_tmp_dir=host_tmp_dir,',
    "        image='dagster-airflow-demo',",
    "        task_id='count__letters_transform',",
    '        s3_conn_id=s3_conn_id,',
    "        command='''-q '",
    '            mutation {{',
    '              startSubplanExecution(',
    '                config: {config},',
    '                executionMetadata: {{',
    '                  runId: "testRun"',
    '                }},',
    '                pipelineName: "demo_pipeline",',
    '                stepExecutions: [',
    '                  {{',
    '                    stepKey: "count_letters.transform"',
    '                  }}',
    '                ],',
    '                marshalledInputs: ',
    '                [',
    '                  {{',
    '                    inputName: "word",',
    '                    key: "/tmp/results/multiply__the__word_transform___result.pickle"',
    '                  }}',
    '                ],',
    '                marshalledOutputs: ',
    '                [',
    '                  {{',
    '                    outputName: "result",',
    '                    key: "/tmp/results/count__letters_transform___result.pickle"',
    '                  }}',
    '                ],',
    '              ) {{',
    '                __typename',
    '              }}',
    "            '",
    "        '''.format(config=CONFIG),",
    '    )',
    '',
    '    multiply__the__word_word_input__thunk_task.set_downstream(multiply__the__word_transform_task)',
    '    multiply__the__word_transform_task.set_downstream(count__letters_transform_task)',
    '',
    '    return dag',
    ''
]

snapshots['test_scaffold_airflow_dag_specify_paths 2'] = [
    "'''Editable scaffolding autogenerated by dagster-airflow from pipeline demo_pipeline with config:",
    '',
    '    context:',
    '      default:',
    '        config: {log_level: DEBUG}',
    '    solids:',
    '      multiply_the_word:',
    '        config: {factor: 2}',
    '        inputs:',
    '          word: {value: bar}',
    '    ',
    '',
    'By convention, users should attempt to isolate post-codegen changes and customizations to this',
    '"editable" file, rather than changing the definitions in the "static" foo.py file. Please let us',
    'know if you are encountering use cases where it is necessary to make changes to the static file.',
    "'''",
    '',
    'import datetime',
    '',
    'from foo import make_dag',
    '',
    '# Arguments to be passed to the ``default_args`` parameter of the ``airflow.DAG`` constructor.You',
    '# can override these with values of your choice.',
    'DEFAULT_ARGS = {',
    "    'depends_on_past': False,",
    "    'email': ['airflow@example.com'],",
    "    'email_on_failure': False,",
    "    'email_on_retry': False,",
    "    'owner': 'airflow',",
    "    'retries': 1,",
    "    'retry_delay': datetime.timedelta(0, 300),",
    '}',
    '',
    '# Any additional keyword arguments to be passed to the ``airflow.DAG`` constructor. You can override',
    '# these with values of your choice.',
    'DAG_KWARGS = {}',
    '',
    '# The name of the autogenerated DAG. By default, this is just the name of the Dagster pipeline from',
    '# which the Airflow DAG was generated (demo_pipeline). You may want to override this if, for',
    '# instance, you want to schedule multiple DAGs corresponding to different configurations of the same',
    '# Dagster pipeline.',
    "DAG_ID = 'demo_pipeline'",
    '',
    '# The description of the autogenerated DAG. By default, this is the description of the Dagster',
    '# pipeline from which the Airflow DAG was generated. You may want to override this, as with the',
    '# DAG_ID parameter.',
    "DAG_DESCRIPTION = '''***Autogenerated by dagster-airflow***'''",
    '',
    '# Additional arguments, if any, to pass to the underlying',
    '# ``dagster_airflow.dagster_plugin.ModifiedDockerOperator`` constructor. Set these if, for instance,',
    '# you need to set special TLS parameters.',
    'MODIFIED_DOCKER_OPERATOR_KWARGS = {}',
    '',
    '# Set your S3 connection id here, if you do not want to use the default ``aws_default`` connection.',
    "S3_CONN_ID = 'aws_default'",
    '',
    '# Set the host directory to mount into /tmp/results on the containers.',
    "HOST_TMP_DIR = '/tmp/results'",
    '',
    'dag = make_dag(',
    '    dag_id=DAG_ID,',
    '    dag_description=DAG_DESCRIPTION,',
    '    dag_kwargs=dict(default_args=DEFAULT_ARGS, **DAG_KWARGS),',
    '    s3_conn_id=S3_CONN_ID,',
    '    modified_docker_operator_kwargs=MODIFIED_DOCKER_OPERATOR_KWARGS,',
    '    host_tmp_dir=HOST_TMP_DIR,',
    ')',
    ''
]

snapshots['test_scaffold_airflow_override_args 1'] = [
    "'''Static scaffolding autogenerated by dagster-airflow from pipeline demo_pipeline with config:",
    '',
    '    context:',
    '      default:',
    '        config: {log_level: DEBUG}',
    '    solids:',
    '      multiply_the_word:',
    '        config: {factor: 2}',
    '        inputs:',
    '          word: {value: bar}',
    '    ',
    '',
    'By convention, users should attempt to isolate post-codegen changes and customizations to the',
    '"editable" demo_pipeline_editable__scaffold.py file, rather than changing the definitions in this',
    '"static" file. Please let us know if you are encountering use cases where it is necessary to make',
    'changes to the static file.',
    "'''",
    '',
    'from airflow import DAG',
    'from airflow.operators.dagster_plugin import DagsterOperator',
    '',
    '',
    "CONFIG = '''",
    '    {',
    '      context: {',
    '        default: {',
    '          config: {',
    '            log_level: "DEBUG"',
    '          }',
    '        }',
    '      },',
    '      solids: {',
    '        multiply_the_word: {',
    '          config: {',
    '            factor: 2',
    '          },',
    '          inputs: {',
    '            word: {',
    '              value: "bar"',
    '            }',
    '          }',
    '        }',
    '      }',
    '    }',
    "'''",
    '',
    '',
    'def make_dag(',
    '    dag_id,',
    '    dag_description,',
    '    dag_kwargs,',
    '    s3_conn_id,',
    '    modified_docker_operator_kwargs,',
    '    host_tmp_dir',
    '):',
    '    dag = DAG(',
    '        dag_id=dag_id,',
    '        description=dag_description,',
    '        **dag_kwargs,',
    '    )',
    '',
    '    multiply__the__word_word_input__thunk_task = DagsterOperator(',
    "        step='multiply_the_word.word.input_thunk',",
    '        config=CONFIG,',
    '        dag=dag,',
    "        tmp_dir='/tmp/results',",
    '        host_tmp_dir=host_tmp_dir,',
    "        image='dagster-airflow-demo',",
    "        task_id='multiply__the__word_word_input__thunk',",
    '        s3_conn_id=s3_conn_id,',
    "        command='''-q '",
    '            mutation {{',
    '              startSubplanExecution(',
    '                config: {config},',
    '                executionMetadata: {{',
    '                  runId: "testRun"',
    '                }},',
    '                pipelineName: "demo_pipeline",',
    '                stepExecutions: [',
    '                  {{',
    '                    stepKey: "multiply_the_word.word.input_thunk"',
    '                  }}',
    '                ],',
    '                marshalledInputs: ',
    '                [',
    '                ],',
    '                marshalledOutputs: ',
    '                [',
    '                  {{',
    '                    outputName: "input_thunk_output",',
    '                    key: "/tmp/results/multiply__the__word_word_input__thunk___input__thunk__output.pickle"',
    '                  }}',
    '                ],',
    '              ) {{',
    '                __typename',
    '              }}',
    "            '",
    "        '''.format(config=CONFIG),",
    '    )',
    '',
    '    multiply__the__word_transform_task = DagsterOperator(',
    "        step='multiply_the_word.transform',",
    '        config=CONFIG,',
    '        dag=dag,',
    "        tmp_dir='/tmp/results',",
    '        host_tmp_dir=host_tmp_dir,',
    "        image='dagster-airflow-demo',",
    "        task_id='multiply__the__word_transform',",
    '        s3_conn_id=s3_conn_id,',
    "        command='''-q '",
    '            mutation {{',
    '              startSubplanExecution(',
    '                config: {config},',
    '                executionMetadata: {{',
    '                  runId: "testRun"',
    '                }},',
    '                pipelineName: "demo_pipeline",',
    '                stepExecutions: [',
    '                  {{',
    '                    stepKey: "multiply_the_word.transform"',
    '                  }}',
    '                ],',
    '                marshalledInputs: ',
    '                [',
    '                  {{',
    '                    inputName: "word",',
    '                    key: "/tmp/results/multiply__the__word_word_input__thunk___input__thunk__output.pickle"',
    '                  }}',
    '                ],',
    '                marshalledOutputs: ',
    '                [',
    '                  {{',
    '                    outputName: "result",',
    '                    key: "/tmp/results/multiply__the__word_transform___result.pickle"',
    '                  }}',
    '                ],',
    '              ) {{',
    '                __typename',
    '              }}',
    "            '",
    "        '''.format(config=CONFIG),",
    '    )',
    '',
    '    count__letters_transform_task = DagsterOperator(',
    "        step='count_letters.transform',",
    '        config=CONFIG,',
    '        dag=dag,',
    "        tmp_dir='/tmp/results',",
    '        host_tmp_dir=host_tmp_dir,',
    "        image='dagster-airflow-demo',",
    "        task_id='count__letters_transform',",
    '        s3_conn_id=s3_conn_id,',
    "        command='''-q '",
    '            mutation {{',
    '              startSubplanExecution(',
    '                config: {config},',
    '                executionMetadata: {{',
    '                  runId: "testRun"',
    '                }},',
    '                pipelineName: "demo_pipeline",',
    '                stepExecutions: [',
    '                  {{',
    '                    stepKey: "count_letters.transform"',
    '                  }}',
    '                ],',
    '                marshalledInputs: ',
    '                [',
    '                  {{',
    '                    inputName: "word",',
    '                    key: "/tmp/results/multiply__the__word_transform___result.pickle"',
    '                  }}',
    '                ],',
    '                marshalledOutputs: ',
    '                [',
    '                  {{',
    '                    outputName: "result",',
    '                    key: "/tmp/results/count__letters_transform___result.pickle"',
    '                  }}',
    '                ],',
    '              ) {{',
    '                __typename',
    '              }}',
    "            '",
    "        '''.format(config=CONFIG),",
    '    )',
    '',
    '    multiply__the__word_word_input__thunk_task.set_downstream(multiply__the__word_transform_task)',
    '    multiply__the__word_transform_task.set_downstream(count__letters_transform_task)',
    '',
    '    return dag',
    ''
]

snapshots['test_scaffold_airflow_override_args 2'] = [
    "'''Editable scaffolding autogenerated by dagster-airflow from pipeline demo_pipeline with config:",
    '',
    '    context:',
    '      default:',
    '        config: {log_level: DEBUG}',
    '    solids:',
    '      multiply_the_word:',
    '        config: {factor: 2}',
    '        inputs:',
    '          word: {value: bar}',
    '    ',
    '',
    'By convention, users should attempt to isolate post-codegen changes and customizations to this',
    '"editable" file, rather than changing the definitions in the "static"',
    'demo_pipeline_static__scaffold.py file. Please let us know if you are encountering use cases where',
    'it is necessary to make changes to the static file.',
    "'''",
    '',
    'import datetime',
    '',
    'from demo_pipeline_static__scaffold import make_dag',
    '',
    '# Arguments to be passed to the ``default_args`` parameter of the ``airflow.DAG`` constructor.You',
    '# can override these with values of your choice.',
    'DEFAULT_ARGS = {',
    "    'depends_on_past': False,",
    "    'email': ['airflow@example.com'],",
    "    'email_on_failure': False,",
    "    'email_on_retry': False,",
    "    'owner': 'airflow',",
    "    'retries': 1,",
    "    'retry_delay': datetime.timedelta(0, 300),",
    '}',
    '',
    '# Any additional keyword arguments to be passed to the ``airflow.DAG`` constructor. You can override',
    '# these with values of your choice.',
    'DAG_KWARGS = {}',
    '',
    '# The name of the autogenerated DAG. By default, this is just the name of the Dagster pipeline from',
    '# which the Airflow DAG was generated (demo_pipeline). You may want to override this if, for',
    '# instance, you want to schedule multiple DAGs corresponding to different configurations of the same',
    '# Dagster pipeline.',
    "DAG_ID = 'demo_pipeline'",
    '',
    '# The description of the autogenerated DAG. By default, this is the description of the Dagster',
    '# pipeline from which the Airflow DAG was generated. You may want to override this, as with the',
    '# DAG_ID parameter.',
    "DAG_DESCRIPTION = '''***Autogenerated by dagster-airflow***'''",
    '',
    '# Additional arguments, if any, to pass to the underlying',
    '# ``dagster_airflow.dagster_plugin.ModifiedDockerOperator`` constructor. Set these if, for instance,',
    '# you need to set special TLS parameters.',
    'MODIFIED_DOCKER_OPERATOR_KWARGS = {}',
    '',
    '# Set your S3 connection id here, if you do not want to use the default ``aws_default`` connection.',
    "S3_CONN_ID = 'aws_default'",
    '',
    '# Set the host directory to mount into /tmp/results on the containers.',
    "HOST_TMP_DIR = '/tmp/results'",
    '',
    'dag = make_dag(',
    '    dag_id=DAG_ID,',
    '    dag_description=DAG_DESCRIPTION,',
    '    dag_kwargs=dict(default_args=DEFAULT_ARGS, **DAG_KWARGS),',
    '    s3_conn_id=S3_CONN_ID,',
    '    modified_docker_operator_kwargs=MODIFIED_DOCKER_OPERATOR_KWARGS,',
    '    host_tmp_dir=HOST_TMP_DIR,',
    ')',
    ''
]
