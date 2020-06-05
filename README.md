# DistributedJobSubmitter
A Distributed System to submit jobs for clients to perform implmented in Django

## client.py
python script to be run on client computers that connects to the job submitting server.
listens for Data being sent from the server and performs the assigned job.
Can be run on a clients machine via the terminal
```bash
python3 client.py
```

## Distributed System
Django project that allows users to select a job to perform which is then submitted to an aviable client to be performed before the result os sent back and displayed to the user.

### Job 1: Monte Carlo Simutlations
Performs Monte Carlo Simulations to estimate the value of PI given a number of iterations to make by the user

### Job 2: Merge Sort
Users can select a file of numbers and submit it to be sorted. The resutling output from the cleint is a downloadable file of the sorted numbers.

## Running the Server
The server can be run by running the follwoing in the terminal
```bash
python manage.py runserver
```
