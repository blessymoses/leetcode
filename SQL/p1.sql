-- account_id, amount, balance_after_transaction, transaction_date
-- For a given account_id and transaction_date, total_transaction_amount, balance in account for a given date

-- 1, 10, 20, 09-02-2022 12:00
-- 1, -5, 15, 09-02-2022 14:00

select *, sum(transaction_amount) over(partition by account_id, transaction_date) from transactions;