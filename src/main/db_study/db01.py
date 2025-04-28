import mariadb

if __name__ == '__main__':
    connection = mariadb.connect(
        host="localhost",
        port=3306,
        user="root",
        password="1q2w3e4r",
        database="webtoon"
    )

    cursor = connection.cursor()

    sql = """
    insert into
        webtoon_tb
    values 
        (default, '월', 'test', 'test_author', '9.9', '이미지url')
    """

    cursor.execute(sql)

    connection.commit()