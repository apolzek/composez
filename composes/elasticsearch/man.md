```bash
curl -X PUT "localhost:9200/example" -H 'Content-Type: application/json' -d'
{
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 0
  }
}
'

for i in $(seq 1 1000); do
  field1=$(shuf -n1 /usr/share/dict/words)
  field2=$(shuf -n1 /usr/share/dict/words)
  field3=$(shuf -n1 /usr/share/dict/words)
  field4=$(shuf -n1 /usr/share/dict/words)
  field5=$(shuf -n1 /usr/share/dict/words)
  field6=$(shuf -n1 /usr/share/dict/words)
  field7=$(shuf -n1 /usr/share/dict/words)
  field8=$(shuf -n1 /usr/share/dict/words)
  field9=$(shuf -n1 /usr/share/dict/words)
  field10=$(shuf -n1 /usr/share/dict/words)

  curl -X POST "localhost:9200/example/_doc" -H 'Content-Type: application/json' -d"
  {
    \"field1\": \"$field1\",
    \"field2\": \"$field2\",
    \"field3\": \"$field3\",
    \"field4\": \"$field4\",
    \"field5\": \"$field5\",
    \"field6\": \"$field6\",
    \"field7\": \"$field7\",
    \"field8\": \"$field8\",
    \"field9\": \"$field9\",
    \"field10\": \"$field10\"
  }
  "
done
```