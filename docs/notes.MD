## Models

 - ### App
    - id (uuid)
    - name (string)
    - description (text)
    - secret_key (string) (Will be used to verify requests between servers)
    - created_at (datetime)
    - updated_at (datetime)

 - ### RegularJob
    - id (uuid)
    - app_id (FK)
    - status (enum([scheduled, running, executed, failed]))
    - retries (integer)
    - attempts (integer)
    - backoff_delay (integer) (milliseconds)
    - backoff_fixed (boolean) (true, backoff_delay = backoff_delay * (2 ** attempts))
    - lambda_webhook_url (string)
    - result_webhook_url (string)
    - created_at (datetime)
    - updated_at (datetime)

 - ### DelayedJob (RegularJob)
    - countdown (integer) (milliseconds)

 - ### ScheduledJob (RegularJob)
    - scheduled_at (datetime)

 - ### RecurrentJob (RegularJob)
    - cron_rule (string)


## API Endpoints

- ### App
    - POST `/api/app` (name, description)
        creates and app and returns the app_data (id, name, description, updated_at, created_at)
    - GET `/api/app/item?guid={guid}`
        returns the app_data (id, name, description, updated_at, created_at)
    - PUT `/api/app/item`
        updates an existing app data          
        requires (X-App-Id, X-Secret-Key headers)
    - DELETE `/api/app/item`
        deletes an existing app             
        requires (X-App-Id, X-Secret-Key headers)
    - GET `/api/app/item/secret-key?guid={guid}`
        returns the secret key of the app
    - POST `/api/app/{id}/secret-key/refresh`
        refreshes and returns the new secret key

- ### Job
    requires (X-App-Id, X-Secret-Key headers)        

    - GET `/api/jobs/{guid}?type=delayed`
        retrieves a job
    - POST `/api/jobs/delay`
        creates a new regular job
    - POST `/api/jobs/countdown`
        creates a new delayed job
    - POST `/api/jobs/schedule`
        creates a new scheduled job
    - POST `/api/jobs/recur`
        creates a new recurrent job
