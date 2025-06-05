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
- [ ] S3 integration
  - [ ] CloudFront
- [ ] S3 write tests

## 📝 Notes

- Using managed Python 3.11 runtime
- Configuration in `apprunner.yaml`
  - DEBUG=True, be careful!
- No Docker/ECS/Fargate required
- Secrets Manager configured and working
- Environment variables set
- Automated startup script with uv and Gunicorn
- Migrations and superuser created automatically