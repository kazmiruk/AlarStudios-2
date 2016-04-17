CREATE TABLE IF NOT EXISTS task (
  id SERIAL PRIMARY KEY,
  timestamp timestamp with time zone
);

TRUNCATE task;

CREATE OR REPLACE FUNCTION init_data() RETURNS void
    LANGUAGE plpgsql
    AS $$
BEGIN
    FOR i IN 1..10 LOOP
        FOR j in 1..2000 LOOP
            INSERT INTO task (timestamp) VALUES (CURRENT_TIMESTAMP - (cast((10 - i) AS varchar) || ' day')::interval);
        END LOOP;
    END LOOP;
END;
$$;

SELECT init_data();
