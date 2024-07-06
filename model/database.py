import pymysql

connection = pymysql.connect(
    host='database-1.c1800c86ily5.ap-northeast-2.rds.amazonaws.com',
    port=3306,
    user='root',
    passwd='Kangbh98!',
    db='test',
    charset='utf8'
)


def get_study_list():
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT study_name, study_goal, study_web_url FROM tb_study WHERE act_year = 2024 AND act_semester = 2"
        cursor.execute(sql)
        result = cursor.fetchall()

        return result


def get_recent_notice():
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT notice_title, notice_date FROM tb_notice LIMIT 5"
        cursor.execute(sql)
        result = cursor.fetchall()

        return result