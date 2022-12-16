/*
 Write a SELECT statement that returns these columns from the Invoices table:
- A column that uses the TRUNCATE function to return the invoice_total column with 1 decimal digit, name it as TruncateInvoiceTotal
- A column that uses the ROUND function to return the invoice_total column with 2 decimal digits, name it as RoundInvoiceTotal
 */

SELECT
    TRUNCATE(invoice_total, 1) AS TruncateInvoiceTotal,
    ROUND(invoice_total, 2) AS RoundInvoiceTotal
FROM invoices;

/*
 Write a SELECT statement that returns these columns from the Vendors table:
- A column that use the UPPER function to return the vendor_city
- A column that displays the last four digits of each phone number
 */

SELECT
    UPPER(vendor_city) AS UpperVendorCity,
    RIGHT(vendor_phone, 4) AS LastFourDigits
FROM vendors;

/*
 Write a SELECT statement that returns these columns from the Vendors table:
- The vendor_name column
- The vendor_name column all in small letters
- The vendor_name column all in capital letters
 */

SELECT
    vendor_name,
    LOWER(vendor_name) AS LowerVendorName,
    UPPER(vendor_name) AS UpperVendorName
FROM vendors;

/*
 Write a SELECT statement that returns these columns from the Invoices table:
- The invoice_number column
- The invoice_date column
- The invoice_date column minus 15 days
- The invoice_date column plus 22 days
 */

SELECT
    invoice_number,
    invoice_date,
    DATE_ADD(invoice_date, INTERVAL -15 DAY) AS InvoiceDateMinus15Days,
    DATE_ADD(invoice_date, INTERVAL 22 DAY) AS InvoiceDatePlus22Days
FROM invoices;

/*
 Write a SELECT statement that returns all columns from the Invoices table WHERE clause that retrieves just the invoices for the month oof May based on the invoice date
 */

SELECT *
FROM invoices
WHERE MONTH(invoice_date) = 5;

/*
 Write a SELECT statement that returns these columns from the Invoices table:
- The invoice_date column
- The column that uses the DATE_FORMAT function to return with day, month name, and four digit year separated by slashes.
 */

SELECT
    invoice_date,
    DATE_FORMAT(invoice_date, '%d/%M/%Y') AS InvoiceDate
FROM invoices;


