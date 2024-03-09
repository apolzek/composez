from prometheus_client import start_http_server, Summary, Counter, Gauge, Histogram
import random
import time

# Inicialize os tipos de métricas
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
REQUEST_COUNTER = Counter('requests_total', 'Total number of requests served')
MEMORY_USAGE = Gauge('memory_usage_bytes', 'Current memory usage in bytes')
TASK_DURATION = Histogram('task_duration_seconds', 'Duration of a task in seconds')

# Inicialize o servidor HTTP para expor as métricas
start_http_server(8000)

# Função que gera métricas falsas
def generate_fake_metrics():
    while True:
        # Gera um tempo de processamento falso
        with REQUEST_TIME.time():
            time.sleep(random.uniform(0.1, 0.5))

        # Incrementa o contador de requisições
        REQUEST_COUNTER.inc()

        # Atualiza o uso de memória fictício
        MEMORY_USAGE.set(random.randint(1000000, 2000000))

        # Adiciona uma duração fictícia de tarefa ao histograma
        TASK_DURATION.observe(random.uniform(0.1, 1.0))

        time.sleep(1)

# Chamada da função para gerar métricas falsas
generate_fake_metrics()
