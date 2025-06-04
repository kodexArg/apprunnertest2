# AppRunner Test 2

Proyecto de pruebas para AWS App Runner con Python 3.11 (sin Docker/ECS).

## 📋 TODO

### Despliegue y Configuración
- [x] Despliegue básico en App Runner
- [x] Configuración de Python 3.11 runtime
- [x] Variables de entorno en apprunner.yaml (SECRET_KEY, ALLOWED_HOSTS, DEBUG)
- [x] Uso de uv para gestión de dependencias
- [x] Gunicorn como servidor WSGI
- [x] Integración con Secrets Manager (PING test)
- [x] Integración con RDS
- [ ] Integración con S3
  - [ ] CloudFront
- [ ] Pruebas escrituras S3


## 📝 Notas

- Usando runtime administrado de Python 3.11
- Configuración en `apprunner.yaml`
  - DEBUG=True, cuidado!
- No se requiere Docker/ECS/Fargate
- Secrets Manager configurado y funcionando
- Variables de entorno establecidas
- Script de inicio automatizado con uv y Gunicorn
- Migraciones y superusuario creados automáticamente