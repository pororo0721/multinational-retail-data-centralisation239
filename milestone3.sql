--Task 1:

ALTER TABLE orders_table
ALTER COLUMN date_uuid TYPE CHAR(36),
ALTER COLUMN user_uuid TYPE CHAR(36),
ALTER COLUMN card_number TYPE VARCHAR(255), 
ALTER COLUMN store_code TYPE VARCHAR(255), 
ALTER COLUMN product_code TYPE VARCHAR(255), 
ALTER COLUMN product_quantity TYPE SMALLINT;

-- Task 2:

SELECT * FROM dim_users WHERE NOT join_date ~ '^\d{4}-\d{2}-\d{2}$';

For example, set invalid dates to NULL
UPDATE dim_users SET join_date = NULL WHERE NOT join_date ~ '^\d{4}-\d{2}-\d{2}$';

ALTER TABLE dim_users
ALTER COLUMN first_name TYPE VARCHAR(255),
ALTER COLUMN last_name TYPE VARCHAR(255),
ALTER COLUMN date_of_birth TYPE DATE USING date_of_birth::DATE,
ALTER COLUMN country_code TYPE VARCHAR(255), 
ALTER COLUMN user_uuid TYPE UUID USING user_uuid::UUID,
ALTER COLUMN join_date TYPE DATE USING join_date::DATE;

-- Task 3:

UPDATE dim_store_details
SET latitude1 = COALESCE(latitude1, latitude2);

ALTER TABLE dim_store_details
DROP COLUMN latitude2;

ALTER TABLE store_details_table
ALTER COLUMN longitude TYPE FLOAT USING longitude::FLOAT,
ALTER COLUMN locality TYPE VARCHAR(255),
ALTER COLUMN store_code TYPE VARCHAR(255), 
ALTER COLUMN staff_numbers TYPE SMALLINT USING staff_numbers::SMALLINT,
ALTER COLUMN opening_date TYPE DATE USING opening_date::DATE,
ALTER COLUMN store_type TYPE VARCHAR(255),
ALTER COLUMN latitude TYPE FLOAT USING latitude::FLOAT,
ALTER COLUMN country_code TYPE VARCHAR(255), 
ALTER COLUMN continent TYPE VARCHAR(255);

UPDATE dim_store_details
SET location = COALESCE(location, 'N/A')
WHERE location IS NULL;

-- Task 4:

--  remove the £ character from the product_price column
UPDATE dim_products
SET product_price = REPLACE(product_price, '£', '');

ALTER TABLE dim_products
ALTER COLUMN product_price TYPE FLOAT USING product_price::FLOAT;

--  add the weight_class column to the products tabl
ALTER TABLE dim_products
ADD COLUMN weight_class VARCHAR(255);

UPDATE dim_products
SET weight_class = 
CASE
    WHEN weight < 2 THEN 'Light'
    WHEN weight >= 2 AND weight < 40 THEN 'Mid_Sized'
    WHEN weight >= 40 AND weight < 140 THEN 'Heavy'
    ELSE 'Truck_Required'
END;

-- Task 5:

--  rename the removed column to still_available
ALTER TABLE dim_products
RENAME COLUMN removed TO still_available;

ALTER TABLE dim_products
ALTER COLUMN product_price TYPE FLOAT USING product_price::FLOAT,
ALTER COLUMN weight TYPE FLOAT USING weight::FLOAT,
ALTER COLUMN EAN TYPE VARCHAR(255), 
ALTER COLUMN product_code TYPE VARCHAR(255), 
ALTER COLUMN date_added TYPE DATE USING date_added::DATE,
ALTER COLUMN uuid TYPE UUID USING uuid::UUID,
ALTER COLUMN still_available TYPE BOOL USING still_available::BOOL,
ALTER COLUMN weight_class TYPE VARCHAR(255); 

-- Task 6:

ALTER TABLE dim_date_times
ALTER COLUMN month TYPE VARCHAR(255), 
ALTER COLUMN year TYPE VARCHAR(255),
ALTER COLUMN day TYPE VARCHAR(255), 
ALTER COLUMN time_period TYPE VARCHAR(n), 
ALTER COLUMN date_uuid TYPE UUID USING date_uuid::UUID;


-- Task 7:

ALTER TABLE dim_card_details
ALTER COLUMN card_number TYPE VARCHAR(255), 
ALTER COLUMN expiry_date TYPE VARCHAR(255), 
ALTER COLUMN date_payment_confirmed TYPE DATE USING date_payment_confirmed::DATE;


-- Task 8:
ALTER TABLE dim_date
ADD PRIMARY KEY (date_uuid);

ALTER TABLE dim_user
ADD PRIMARY KEY (user_uuid);

ALTER TABLE dim_card_details
ADD PRIMARY KEY (card_number);

ALTER TABLE dim_store
ADD PRIMARY KEY (store_code);

ALTER TABLE dim_product
ADD PRIMARY KEY (product_code);



-- Task 9:

ALTER TABLE orders_table
ADD FOREIGN KEY (date_uuid) REFERENCES dim_date(date_uuid),
ADD FOREIGN KEY (user_uuid) REFERENCES dim_user(user_uuid),
ADD FOREIGN KEY (card_number) REFERENCES dim_card_details(card_number),
ADD FOREIGN KEY (store_code) REFERENCES dim_store(store_code),
ADD FOREIGN KEY (product_code) REFERENCES dim_product(product_code);