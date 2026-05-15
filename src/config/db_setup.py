from sqlalchemy import create_engine, text

def ensure_database_exists(admin_url: str, db_name: str):
    """Se encarga exclusivamente de verificar y crear el contenedor físico."""
    engine = create_engine(admin_url, isolation_level="AUTOCOMMIT")
    with engine.connect() as conn:
        exists = conn.execute(
            text(f"SELECT 1 FROM pg_database WHERE datname='{db_name}'")
        ).scalar()
        
        if not exists:
            conn.execute(text(f"CREATE DATABASE {db_name}"))
    engine.dispose()