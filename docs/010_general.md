# Django Reference

## Project structure

-   **/routes**: Api routes extensions (Custom endpoints definitions)
-   **/domain**: Business logic methods
-   **/models/fixtures**: Initial data inserts (e.g. dummy data and catalogs)
-   /models: Data model extensions. (Database model representation)
-   /app/settings.py: Django settings
-   /seed: Autogenerated files produced by seed-builder: It includes model definitions, CRUD endpoint creation, serializers and graphql implementation
    >   *These files are *read-only*, modifiable only through [seed-builder](./060_seed_builder.md)*
    
## Development
    
### Database management

-   To update database (migration, fixtures) execute `bin/update.sh` (For windows `bin/update.bat`)
-   To open db manager (psql) execute `bin/query.sh` (For windows `bin/query.bat`)

### Testing & QA

-   Test use cases `bin/test.sh` (For windows `bin/test.bat`)
-   Review code quality `bin/review.sh` (For windows `bin/review.bat`)
    >   To run review command, install [Codacy CLI](https://github.com/codacy/codacy-analysis-cli)
-   Generate code coverage report `bin/coverage.sh` (For windows `bin/coverage.bat`)

### Deployment (dev stage)

-  To upload to development server
    -  Request a .pem.dev and a port-key to system admin
    -  Paste .pem.dev in root directory of the project
    -  Execute `bin/deploy.sh <PORT-KEY>` (For windows `bin/deploy.sh <PORT-KEY>`)
    
### Docker

-   Clean unused docker resources `bin/clean.sh` (For windows `bin/clean.bat`)

## Other resources

-   [Routes docs](./020_routes.md)
-   [Domain docs](./030_domain.md)
-   [Models docs](./040_models.md)
-   [Seed builder](./060_seed_builder.md)