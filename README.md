# Overlap Verificaton

## Usage
```bash
python schedule.py [schedule]
```
where `schedule` is optional parameter for CSV file. Default set to `.csv/schedule.csv`

## Tests
The following scenarios were assumed (`|-----|` represents single event/meeting ):
1. No event overlaps
```
|-----| <---> |-----|
```

2. No event overlaps, adjacent events
```
|-----||-----|
```

3. Single overlap opt1
```
|-----|
   |-----|
```

4. Single overlap opt2
```
|----------------|
   |-----|
```

5. Multiple overlaps opt1
```
|-----------------------------|
   |-----| <---> |--------|
```

6. Multiple overlaps opt2
```
|-----------------------------|
   |----------| 
        |-----------|
```

7. Multiple overlaps opt3, event doesn't have an end specified. 
   In this case it defaults to 2030-01-01::00:00
   
```
|----------------------------------------
   |-----------------|
```