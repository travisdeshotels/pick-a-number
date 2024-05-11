# Pick A Number API

Register  
`curl -d '{"userName":"me", "email":"foo@bar.goof"}' -H "Content-Type: application/json" -X POST http://localhost:8000/register`  
Play  
`curl -H "Content-Type: application/json" -H "Secret: ${SECRETID}" -X GET http://localhost:8000/?guess=3`  
Scoreboard  
`curl -X GET http://localhost:8000/scores`

## Docker
`docker build -t numbergame .`  
`docker run --name game -p 8000:8000 numbergame`
