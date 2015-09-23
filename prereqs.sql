CREATE TABLE prerequisite (
	`CRN` INTEGER NOT NULL,
	`Hours` INTEGER,
	`GPA` DOUBLE,
	`Classes` TEXT,
	`Major Code1` VARCHAR(4),
	primary key(`CRN`)
);

ALTER TABLE student ADD `Major Code1` VARCHAR(4);

update student s set s.`Major Code1` = r.`Major Code1` from registrations r where r.`Banner Id` = s.`Banner Id`;

