from rx import Observable
from graphql_ws.gevent import GeventSubscriptionServer, SubscriptionObserver


class DagsterSubscriptionServer(GeventSubscriptionServer):
    '''Subscription server that is able to handle non-subscription commands'''

    def __init__(self, *args, **kwargs):
        super(GeventSubscriptionServer, self).__init__(*args, **kwargs)

    def execute(self, request_context, params):
        # https://github.com/graphql-python/graphql-ws/issues/7
        params['context_value'] = request_context
        return super(GeventSubscriptionServer, self).execute(request_context, params)

    def on_start(self, connection_context, op_id, params):
        try:
            execution_result = self.execute(connection_context.request_context, params)
            if not isinstance(execution_result, Observable):
                observable = Observable.of(execution_result)
            else:
                observable = execution_result
            observable.subscribe(
                SubscriptionObserver(
                    connection_context, op_id, self.send_execution_result, self.send_error,
                    self.on_close
                )
            )
        except Exception as e:
            self.send_error(connection_context, op_id, str(e))