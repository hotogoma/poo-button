CREATE SCHEMA data;

CREATE TABLE data.baby_events (
    time timestamp without time zone NOT NULL DEFAULT CURRENT_TIMESTAMP,
    type character varying NOT NULL
);

CREATE INDEX baby_events_time_idx ON data.baby_events(time timestamp_ops);
CREATE INDEX baby_events_type_idx ON data.baby_events(type text_ops);
