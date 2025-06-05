# AppRunner Test 2

Test project for AWS App Runner with Python 3.11 (without Docker/ECS).

## 📋 TODO

### Deployment and Configuration
- [x] Basic App Runner deployment
- [x] Python 3.11 runtime configuration
- [x] Environment variables in apprunner.yaml (SECRET_KEY, ALLOWED_HOSTS, DEBUG)
- [x] Using uv for dependency management
- [x] Gunicorn as WSGI server
- [x] Secrets Manager integration (PING test)
- [x] RDS integration
- [x] S3 integration
  - [x] CloudFront
- [x] S3 write tests

## 📝 Notes

- Using managed Python 3.11 runtime
- Configuration in `apprunner.yaml`
  - DEBUG=True, be careful!
- No Docker/ECS/Fargate required
- Secrets Manager configured and working
- Environment variables set
- Automated startup script with uv and Gunicorn
- Migrations and superuser created automatically
- **Explicit and detailed test suite:**
  - S3 integration and write tests implemented and passing
  - Application tests for views and models are run explicitly and provide detailed logs

## 4. Ejecución explícita y detallada de tests

### 4.1. Ejecutar los tests de vistas (`test_views.py`)

1. Inicia la ejecución de los tests de vistas:
   ```sh
   python manage.py test core.tests.test_views
   ```
2. Observa la salida:
   - Verás los logs de Loguru para cada test.
   - Se informará el inicio y fin de cada test, así como los resultados (OK, FAIL, ERROR).

### 4.2. Ejecutar los tests de modelos (`test_models.py`)

1. Inicia la ejecución de los tests de modelos:
   ```sh
   python manage.py test core.tests.test_models
   ```
2. Observa la salida:
   - Verás los logs de Loguru para cada test de modelo.
   - Se informará el inicio y fin de cada test, así como los resultados.

### 4.3. (Opcional) Automatizar la ejecución secuencial

Si quieres ejecutar ambos archivos de forma secuencial y ver los resultados uno tras otro, puedes usar un pequeño script:

**Bash:**
```sh
echo "Ejecutando tests de vistas..."
python manage.py test core.tests.test_views
echo "Ejecutando tests de modelos..."
python manage.py test core.tests.test_models
```

**PowerShell:**
```powershell
Write-Host "Ejecutando tests de vistas..."
python manage.py test core.tests.test_views
Write-Host "Ejecutando tests de modelos..."
python manage.py test core.tests.test_models
```

### 4.4. (Opcional) Agregar logs adicionales

Si deseas aún más detalle, puedes agregar logs en cada método de test para indicar pasos intermedios, por ejemplo:

```python
def test_algo(self):
    logger.info("Preparando test_algo")
    # ... test ...
    logger.info("Finalizó test_algo")
```