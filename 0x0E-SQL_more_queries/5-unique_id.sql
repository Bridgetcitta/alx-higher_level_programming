-- Creates a table unique_id on MySQL server
-- if the table unique_id already exits, the script should not fail.
CREATE TABLE IF NOT EXISTS `unique_id` (
    `id`   INT          DEFAULT 1 UNIQUE,
    `name` VARCHAR(256)
);
