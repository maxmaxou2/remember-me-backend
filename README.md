# remember-me-backend
Capture your wisdom, share it with your family

# Pre-Requirements

- Python 3.12
- PostgreSQL

# Setup

1. Clone the repository
```bash
git clone git@github.com:maxmaxou2/remember-me-backend.git
cd remember-me-backend
```

2. Install dependencies
```bash
make install
```

3. Create dev and testing databases
```bash
createdb -U postgres remember_me_backend
remember-me init-db
createdb -U postgres remember_me_backend_unittest
```

# Run the server
```bash
make dev
```
