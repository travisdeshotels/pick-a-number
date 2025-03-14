Register
```
SECRETID=$(curl -d '{"userName":"me", "email":"foo@bar.goof"}' -H "Content-Type: application/json" -X POST http://localhost:8000/register | jq -r .secretId)
```
Play
```
curl -H "Secret: ${SECRETID}" -X GET http://localhost:8000/?guess=3 | jq
```
Scoreboard
```
curl -X GET http://localhost:8000/scores | jq
```
