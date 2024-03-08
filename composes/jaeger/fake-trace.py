from jaeger_client import Config
import time

def create_traces_with_trace(service_name, host, port, num_traces):
    config = Config(
        config={
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'local_agent': {
                'reporting_host': host,
                'reporting_port': port,
            },
            'logging': True,
        },
        service_name=service_name,
    )

    tracer = config.initialize_tracer()

    for i in range(num_traces):
        with tracer.start_span(f'parent-span-{i}') as parent_span:
            parent_span.log_kv({'event': 'parent-start', 'value': i})

            with tracer.start_span('child-span-1', child_of=parent_span) as child_span1:
                child_span1.log_kv({'event': 'child-1-start'})
                time.sleep(0.05)  # Simula algum trabalho
                child_span1.log_kv({'event': 'child-1-end'})

            with tracer.start_span('child-span-2', child_of=parent_span) as child_span2:
                child_span2.log_kv({'event': 'child-2-start'})
                time.sleep(0.05)  # Simula algum trabalho
                child_span2.log_kv({'event': 'child-2-end'})

            parent_span.log_kv({'event': 'parent-end'})

    tracer.close()

if __name__ == '__main__':
    create_traces_with_trace('fake-service', 'localhost', 6831, 1000)
