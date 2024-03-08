import os
import yaml
import json

def find_docker_compose_files(directory):
    docker_compose_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == 'docker-compose.yaml':
                docker_compose_files.append(os.path.join(root, file))
    return docker_compose_files

def generate_readme(directory):
    readme_content = "# Docker Compose Services\n\nThis file was generated automatically\n\n"
    docker_compose_files = find_docker_compose_files(directory)
    for file in docker_compose_files:
        folder_name = os.path.basename(os.path.dirname(file))
        readme_content += "### " + folder_name + "\n\n"
        readme_content += "```\n"
        readme_content += "docker-compose -f " + file + " up -d\n"
        readme_content += "docker-compose -f " + file + " down\n"
        readme_content += "docker-compose -f " + file + " ps\n"  # Adiciona a linha ps
        readme_content += "```\n\n"
        with open(file, 'r') as f:
            data = f.read()
            docker_compose_data = yaml.safe_load(data)
            services = []
            for service_name, service_data in docker_compose_data.get('services', {}).items():
                ports = service_data.get('ports', [])
                ports_str = [str(port) for port in ports]
                services.append({"name": service_name, "ports": ports_str})
            services_json = json.dumps({"services": services}, indent=2)
            readme_content += "```json\n"
            readme_content += services_json + "\n"
            readme_content += "```\n\n"

    with open('composes.md', 'w') as f:
        f.write(readme_content)

directory = 'composes/'
generate_readme(directory)
