terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

# Criar a imagem Docker a partir do Dockerfile
resource "docker_image" "my_app" {
  name = "meu_app:latest"
  build {
    context    = "."    # Diretório onde está o Dockerfile
    dockerfile = "Dockerfile"
  }
}

# Criar um container a partir da imagem
resource "docker_container" "my_container" {
  name  = "meu_container"
  image = docker_image.my_app.image_id

  # Mantém o container aberto
  tty        = true
  stdin_open = true

  ports {
    internal = 80
    external = 8080
  }
}
