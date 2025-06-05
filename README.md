# AppRunner Test 2

Test project for AWS App Runner with Python 3.11 (without Docker/ECS).


## 📋 Implementation Order

### 1. Core Infrastructure
- [x] Basic App Runner deployment
- [x] Python 3.11 runtime configuration
- [x] Environment variables in apprunner.yaml (SECRET_KEY, ALLOWED_HOSTS, DEBUG)
- [x] Using uv for dependency management
- [x] Gunicorn as WSGI server
- [ ] Local development environment setup
  - [ ] Development settings configuration
  - [ ] Local database setup
  - [ ] Local S3 emulation
  - [ ] Development scripts and tools

### 2. AWS Services Integration
- [x] Secrets Manager integration (PING test)
- [x] RDS integration
- [x] S3 integration
  - [x] CloudFront
- [x] S3 write tests

### 3. Application Features
- [x] Template structure and organization
  - [x] Common `/templates` directory
  - [x] App-specific templates
- [ ] User Structure
  - [ ] Authentication System
    - [ ] Login/Logout views
    - [ ] Password reset flow
  - [ ] Testing
- [ ] API Structure
  - [ ] Design and Implementation
    - [ ] Set up authentication
    - [ ] Create core endpoints
  - [ ] Testing

### 4. Frontend
- [ ] Setup Frontend Stack
  - [ ] Django-components
  - [ ] Vite
  - [ ] Tailwind
  - [ ] HTMX
- [ ] Custom Components Library for this project
  - [ ] Base components / Templates
    - [ ] Include HTMX strategy
  - [ ] Build and test core components


## 📝 Notes

- Configuration in `apprunner.yaml`
  - DEBUG=True, be careful!
- No Docker/ECS/Fargate required
- Automated startup (/scripts/startup.sh) with tests, uv and Gunicorn
- Migrations and superuser created automatically
- **Explicit and detailed test suite:**
  - S3 integration and write tests implemented and passing
  - Application tests for views and models are run explicitly and provide detailed logs
- **Frontend Implementation Notes:**
  - Modern stack: Vite + Tailwind + HTMX + Components
  - Progressive enhancement approach
  - Static assets served through CloudFront
  - Build process integrated with AppRunner deployment
- **API Implementation Notes:**
  - RESTful design principles
  - JWT-based authentication
  - Rate limiting and caching
  - Comprehensive test coverage
- **User System Notes:**
  - Django's built-in authentication
  - Custom user model for extensibility
  - Secure password handling
  - Session management


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.