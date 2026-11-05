-- TASK : GTM Lead Filtering
-- Dataset: leads (1,200 fictional records)

-- Task 1: Find leads from Pakistan.
-- Purpose: Identify prospects in a target country.

SELECT first_name, last_name, country, work_email
FROM leads
WHERE country = 'Pakistan';


-- Task 2: Find leads from the United States.
-- Purpose: Review their job titles and statuses.

SELECT first_name, last_name, job_title, lead_status
FROM leads
WHERE country = 'United States';


-- Task 3: Find qualified leads from Pakistan.
-- Purpose: Identify leads ready for further review.

SELECT *
FROM leads
WHERE country = 'Pakistan'
AND lead_status = 'Qualified';


-- Task 4: Find leads not marked as Qualified.
-- Purpose: Review leads needing further qualification.

SELECT *
FROM leads
WHERE lead_status <> 'Qualified';
