import mysql.connector
from mysql.connector import Error
import time
import random

class Database:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'ПОЛЬЗОВАТЕЛЬ'
        self.password = 'ПАРОЛЬ'
        self.database = 'БАЗА ДАННЫХ'
        self.connection = None
        self.cursor = None
        self.max_retries = 3  # Максимальное количество попыток переподключения
        self.retry_delay = 5  # Задержка между попытками переподключения в секундах

    def connect(self):
        retries = 0
        while retries < self.max_retries:
            try:
                self.connection = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
                )
                if self.connection.is_connected():
                    self.cursor = self.connection.cursor(dictionary=True)  
                    print("Connected to MySQL database")
                    return
            except Error as e:
                print(f"Error connecting to MySQL (attempt {retries + 1}/{self.max_retries}): {e}")
                retries += 1
                time.sleep(self.retry_delay)
        
        # Если все попытки провалились, выбрасываем исключение
        raise Exception(f"Failed to connect to MySQL after {self.max_retries} retries.")


    def disconnect(self):
      if self.connection and self.connection.is_connected():
        try:
            self.cursor.close()
            self.connection.close()
            print("MySQL connection closed")
        except Error as e:
            print(f"Error closing connection: {e}")
        finally:
            self.connection = None
            self.cursor = None

    def _ensure_connection(self):
        """ Проверяет соединение и переподключается, если необходимо """
        if not self.connection or not self.connection.is_connected():
           self.connect()
    
    def execute_query(self, query, params=None):
        try:
            self._ensure_connection()
            self.cursor.execute(query, params)
            self.connection.commit()
            return self.cursor
        except Error as e:
            print(f"Error executing query: {e}")
            raise

    def fetch_all(self, query, params=None):
        try:
            self._ensure_connection()
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except Error as e:
            print(f"Error fetching data: {e}")
            raise

    def fetch_one(self, query, params=None):
        try:
             self._ensure_connection()
             self.cursor.execute(query, params)
             return self.cursor.fetchone()
        except Error as e:
            print(f"Error fetching single row: {e}")
            raise


    # Методы для конкретных запросов
    def add_user(self, telegram_id):
            query = 'INSERT INTO users (telegram_id) VALUES (%s) ON DUPLICATE KEY UPDATE telegram_id = VALUES(telegram_id)'
            params = (telegram_id,)
            self.execute_query(query, params)