# remember-me-backend
Capture your wisdom, share it with your family

# Setup

1. Clone the repository
```bash
git clone https://github.com/maxence-ho/remember-me-backend.git
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

4. Run the server
```bash
make dev
```
