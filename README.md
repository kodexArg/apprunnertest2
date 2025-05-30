# AppRunner Test 2

Prueba de despliegue en AWS App Runner (sin Docker)

**Repositorio:** https://github.com/kodexArg/apprunnertest2/

## ⚙️ Configuración

- Despliegue exclusivo en AWS App Runner (runtime administrado Python 3.11)
- Configuración principal: `apprunner.yaml`
- Sin Docker, ECS, Fargate ni EC2

## 📁 Estructura del Proyecto

```
├── apprunner.yaml         # Configuración App Runner
├── requirements.txt       # Dependencias Python
├── manage.py              # Django
├── project/               # Proyecto Django
├── core/                  # App principal
└── README.md
```

## 🚀 Despliegue en App Runner

- App Runner construye y ejecuta usando Python 3.11
- La app escucha en `0.0.0.0:$PORT` (por defecto: 8080)
- Ejemplo de configuración:

```yaml
version: 1.0
runtime: python311
build:
  commands:
    build:
      - pip3 install -r requirements.txt
run:
  runtime-version: 3.11
  command: gunicorn -b 0.0.0.0:8080 project.wsgi
  network:
    port: 8080
```

- `gunicorn` y `boto3` deben estar en `requirements.txt`

## 🔐 Uso de Secrets Manager (PING)

La aplicación utiliza un secret de AWS Secrets Manager llamado `PING` (ARN configurado en `apprunner.yaml`). El valor de este secret se muestra en la página principal junto al mensaje Hello World.

Ejemplo de configuración en `apprunner.yaml`:

```yaml
run:
  # ...
  secrets:
    - name: PING
      value-from: "arn:aws:secretsmanager:us-east-1:789650504128:secret:pingping/secret-VcQsw5"
```

En la vista principal se mostrará:

```
Hello World - PING: PONG
```

## ✅ Estado

- Versión funcional: successfully deployed to apprunnertest2
- Tag: `