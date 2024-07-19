import pymysql


def run_query(sql):
    connection = pymysql.connect(
        host='forifdb.c1800c86ily5.ap-northeast-2.rds.amazonaws.com',
        port=3306,
        user='root',
        passwd='Kangbh98!',
        db='dev',
        charset='utf8'
    )

    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()

        connection.commit()

        return result

    finally:
        connection.close()


def get_study_list():
    sql = '''
    SELECT study_name, explanation, img_url, web_url
    FROM tb_study
    WHERE act_year = 2024
    AND act_semester = 2;
    '''

    return run_query(sql)


def get_recent_notice():
    sql = '''
    SELECT title, created_at
    FROM tb_post
    WHERE post_type = '공지사항'
    LIMIT 5;
    '''

    return run_query(sql)