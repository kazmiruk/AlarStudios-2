# AlarStudios-2

II. Python/SQL удаление “большого” объема данных из RDBMS.

а) Предположим, что в некой таблице сотни миллионов записей и “неудобные” индексы. 

б) Таблица используется постоянно и возможности занять ее локом на запись хоть сколь нибудь надолго нельзя никак. Необходимо “почистить” таблицу соблюдая эти условия. 

в) Стирать записи малыми кусками (например, по 100), эффективно их находя (т.е., не sequental scan), беря и полностью освобождая локи и со случайной (пара сотен миллисекунд) паузой между удалениями. 

г) Таблица должна иметь поля: ID и Timestamp. 

д) Стереть необходимо записи за 5 (из 10-и) дней. 

е) SQLAlchemy с raw запросами. PostgreSQL или MySQL. 

ж) Сид базы - произвольная таблица с парой десятков тысячь записей, с Timestamp ровномерно распределенным на 10 дней.
