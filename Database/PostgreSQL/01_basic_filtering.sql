-- Task 1: Retrieve leads from Pakistan.
-- GTM purpose: Identify prospects by geographic market.

SELECT first_name, last_name, work_email
FROM leads
WHERE country = 'Pakistan';


-- Task 2: Count Pakistani leads.
-- GTM purpose: Estimate the size of this prospect segment.

SELECT COUNT(*)
FROM leads
WHERE country = 'Pakistan';
