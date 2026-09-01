-- Operational metrics for the generated roster

SELECT
    flight_id,
    COUNT(*) AS unassigned_positions
FROM roster
WHERE crew_id = 'UNASSIGNED'
GROUP BY flight_id;

SELECT
    crew_id,
    COUNT(*) AS sectors,
    SUM(block_hours) AS block_hours
FROM roster
WHERE crew_id <> 'UNASSIGNED'
GROUP BY crew_id
ORDER BY block_hours DESC;

SELECT
    role,
    COUNT(*) AS assignments
FROM roster
WHERE crew_id <> 'UNASSIGNED'
GROUP BY role;
