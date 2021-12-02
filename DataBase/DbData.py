"""
Переменные и тексты запросов для работы с базой данных

PATH - путь к БД
CREATE_DB - запрос на создание БД при первом запуске
"""

PATH = "DataBase\\eToken.db"

CREATE_DB = f"""
            CREATE TABLE IF NOT EXISTS jrn (
            id_record INTEGER PRIMARY KEY AUTOINCREMENT not null,
            sn CHAR,
            type_device CHAR,
            num_akt CHAR ,
            roo smallint,
            roo_dop char ,
            date_to date,
            time_to time,
            id_adm smallint,
            num_jrn integer,
            date_reg date,
            tojrn char,
            foreign key (roo) references spr_roo(id),
            foreign key (id_adm) references admins(id_admin));

            CREATE TABLE IF NOT EXISTS spr_roo (
            id INTEGER PRIMARY KEY AUTOINCREMENT not null,
            name_roo char );

            CREATE TABLE IF NOT EXISTS admins (
            id_admin INTEGER PRIMARY KEY AUTOINCREMENT not null,
            adm_login char 
            adm_fio char
            adm_dolg char );
            """