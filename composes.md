# Docker Compose Services

This file was generated automatically

### tomcat

```
docker-compose -f composes/tomcat/docker-compose.yaml up -d
docker-compose -f composes/tomcat/docker-compose.yaml down
docker-compose -f composes/tomcat/docker-compose.yaml ps
```

```json
{
  "services": [
    {
      "name": "tomcat",
      "ports": [
        "8080:8080"
      ]
    }
  ]
}
```

### mockserver

```
docker-compose -f composes/mockserver/docker-compose.yaml up -d
docker-compose -f composes/mockserver/docker-compose.yaml down
docker-compose -f composes/mockserver/docker-compose.yaml ps
```

```json
{
  "services": [
    {
      "name": "mockserver",
      "ports": [
        "1080:1080"
      ]
    }
  ]
}
```

### toxiproxy

```
docker-compose -f composes/toxiproxy/docker-compose.yaml up -d
docker-compose -f composes/toxiproxy/docker-compose.yaml down
docker-compose -f composes/toxiproxy/docker-compose.yaml ps
```

```json
{
  "services": [
    {
      "name": "toxiproxy",
      "ports": [
        "8474:8474",
        "8800:8800",
        "8801:8801",
        "8802:8802"
      ]
    },
    {
      "name": "toxiproxy-ui",
      "ports": [
        "8484:8080"
      ]
    }
  ]
}
```

### redis

```
docker-compose -f composes/redis/docker-compose.yaml up -d
docker-compose -f composes/redis/docker-compose.yaml down
docker-compose -f composes/redis/docker-compose.yaml ps
```

```json
{
  "services": [
    {
      "name": "redis",
      "ports": [
        "6379:6379"
      ]
    }
  ]
}
```

### nginx

```
docker-compose -f composes/nginx/docker-compose.yaml up -d
docker-compose -f composes/nginx/docker-compose.yaml down
docker-compose -f composes/nginx/docker-compose.yaml ps
```

```json
{
  "services": [
    {
      "name": "nginx",
      "ports": [
        "80:80"
      ]
    }
  ]
}
```

### portainer

```
docker-compose -f composes/portainer/docker-compose.yaml up -d
docker-compose -f composes/portainer/docker-compose.yaml down
docker-compose -f composes/portainer/docker-compose.yaml ps
```

```json
{
  "services": [
    {
      "name": "portainer",
      "ports": [
        "8000:8000",
        "9443:9443"
      ]
    }
  ]
}
```

### elasticsearch

```
docker-compose -f composes/elasticsearch/docker-compose.yaml up -d
docker-compose -f composes/elasticsearch/docker-compose.yaml down
docker-compose -f composes/elasticsearch/docker-compose.yaml ps
```

```json
{
  "services": [
    {
      "name": "elasticsearch",
      "ports": [
        "9200:9200",
        "9300:9300"
      ]
    },
    {
      "name": "kibana",
      "ports": [
        "5601:5601"
      ]
    }
  ]
}
```

### uptime-kuma

```
docker-compose -f composes/uptime-kuma/docker-compose.yaml up -d
docker-compose -f composes/uptime-kuma/docker-compose.yaml down
docker-compose -f composes/uptime-kuma/docker-compose.yaml ps
```

```json
{
  "services": [
    {
      "name": "uptime-kuma",
      "ports": [
        "3001:3001"
      ]
    }
  ]
}
```

### mongo

```
docker-compose -f composes/mongo/docker-compose.yaml up -d
docker-compose -f composes/mongo/docker-compose.yaml down
docker-compose -f composes/mongo/docker-compose.yaml ps
```

```json
{
  "services": [
    {
      "name": "db",
      "ports": [
        "27017:27017"
      ]
    },
    {
      "name": "mongo-express",
      "ports": [
        "8081:8081"
      ]
    }
  ]
}
```

### prometheus

```
docker-compose -f composes/prometheus/docker-compose.yaml up -d
docker-compose -f composes/prometheus/docker-compose.yaml down
docker-compose -f composes/prometheus/docker-compose.yaml ps
```

```json
{
  "services": [
    {
      "name": "prometheus",
      "ports": [
        "9090:9090"
      ]
    }
  ]
}
```

### zipkin

```
docker-compose -f composes/zipkin/docker-compose.yaml up -d
docker-compose -f composes/zipkin/docker-compose.yaml down
docker-compose -f composes/zipkin/docker-compose.yaml ps
```

```json
{
  "services": [
    {
      "name": "zipkin",
      "ports": [
        "9411:9411"
      ]
    }
  ]
}
```

### maildev

```
docker-compose -f composes/maildev/docker-compose.yaml up -d
docker-compose -f composes/maildev/docker-compose.yaml down
docker-compose -f composes/maildev/docker-compose.yaml ps
```

```json
{
  "services": [
    {
      "name": "maildev",
      "ports": [
        "80:80",
        "25:25"
      ]
    }
  ]
}
```

### nexus

```
docker-compose -f composes/nexus/docker-compose.yaml up -d
docker-compose -f composes/nexus/docker-compose.yaml down
docker-compose -f composes/nexus/docker-compose.yaml ps
```

```json
{
  "services": [
    {
      "name": "nexus",
      "ports": [
        "8081:8081"
      ]
    }
  ]
}
```

### glances

```
docker-compose -f composes/glances/docker-compose.yaml up -d
docker-compose -f composes/glances/docker-compose.yaml down
docker-compose -f composes/glances/docker-compose.yaml ps
```

```json
{
  "services": [
    {
      "name": "glances",
      "ports": []
    }
  ]
}
```

### jaeger

```
docker-compose -f composes/jaeger/docker-compose.yaml up -d
docker-compose -f composes/jaeger/docker-compose.yaml down
docker-compose -f composes/jaeger/docker-compose.yaml ps
```

```json
{
  "services": [
    {
      "name": "jaeger",
      "ports": [
        "6831:6831/udp",
        "16686:16686"
      ]
    }
  ]
}
```

### graphite

```
docker-compose -f composes/graphite/docker-compose.yaml up -d
docker-compose -f composes/graphite/docker-compose.yaml down
docker-compose -f composes/graphite/docker-compose.yaml ps
```

```json
{
  "services": [
    {
      "name": "graphite",
      "ports": [
        "80:80",
        "2003:2003",
        "2004:2004",
        "2023:2023",
        "2024:2024",
        "8125:8125",
        "8126:8126"
      ]
    }
  ]
}
```

### mitmproxy

```
docker-compose -f composes/mitmproxy/docker-compose.yaml up -d
docker-compose -f composes/mitmproxy/docker-compose.yaml down
docker-compose -f composes/mitmproxy/docker-compose.yaml ps
```

```json
{
  "services": [
    {
      "name": "mitmproxy",
      "ports": [
        "8080:8080",
        "8081:8081"
      ]
    }
  ]
}
```

### rabbitmq

```
docker-compose -f composes/rabbitmq/docker-compose.yaml up -d
docker-compose -f composes/rabbitmq/docker-compose.yaml down
docker-compose -f composes/rabbitmq/docker-compose.yaml ps
```

```json
{
  "services": [
    {
      "name": "rabbitmq",
      "ports": [
        "5672:5672",
        "15672:15672"
      ]
    }
  ]
}
```

