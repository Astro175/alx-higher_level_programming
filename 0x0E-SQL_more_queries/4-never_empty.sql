--- Script that creates a table and makes its ID value default of 1
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256)
);
