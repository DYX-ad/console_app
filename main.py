from providers.raw_sql_provider import RawSqlProvider
from providers.sqlalchemy_provider import SqlAlchemyProvider
from ui_logic.console_ui import ConsoleDbApp


def main():
    app = ConsoleDbApp(RawSqlProvider, SqlAlchemyProvider)
    app.start_app()


if __name__ == '__main__':
    main()