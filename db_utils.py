import pymysql
import hashlib

HOST = "localhost"
USER = "root"
PASSWD = "root"
DATABASE = "polyclinic"


def check_connection():
    try:
        db = pymysql.connect(host=HOST, user=USER, passwd=PASSWD, database=DATABASE)
        db.close()
        return True, 0
    except pymysql.err.OperationalError as e:
        return False, e


def check_credentials(login, passwd):
    db = pymysql.connect(host=HOST, user=USER, passwd=PASSWD, database=DATABASE)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `patient` WHERE 1")
    result = cursor.fetchall()
    for i in range(len(result)):
        if result[i][1] == login:
            hp = str(hashlib.sha256(passwd.encode('utf-8')).hexdigest())
            if result[i][2] == hp:
                db.close()
                return True
    db.close()
    return False


def check_login_exists(login):
    db = pymysql.connect(host=HOST, user=USER, passwd=PASSWD, database=DATABASE)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `patient` WHERE 1")
    result = cursor.fetchall()
    for i in range(len(result)):
        if result[i][1] == login:
            return True
    db.close()
    return False


def add_patient(login, passwd, name, insurance):
    db = pymysql.connect(host=HOST, user=USER, passwd=PASSWD, database=DATABASE)
    cursor = db.cursor()
    cursor.execute("SELECT `Id` FROM `patient` WHERE 1")
    result = cursor.fetchall()
    new_id = result[len(result) - 1][0] + 1
    hs = hashlib.sha256(passwd.encode('utf-8')).hexdigest()
    sql = f"INSERT INTO `patient` (`Id`, `Login`, `Password`, `Name`, `Insurance`) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (int(new_id), str(login), str(hs), str(name), insurance))
    db.commit()
    db.close()


def give_name_by_login(login):
    db = pymysql.connect(host=HOST, user=USER, passwd=PASSWD, database=DATABASE)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `patient` WHERE 1")
    result = cursor.fetchall()
    for i in range(len(result)):
        if result[i][1] == login:
            db.close()
            return result[i][3]


def get_id_patient(login):
    db = pymysql.connect(host=HOST, user=USER, passwd=PASSWD, database=DATABASE)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `patient` WHERE 1")
    result = cursor.fetchall()
    for i in range(len(result)):
        if result[i][1] == login:
            db.close()
            return result[i][0]


def get_doctors():
    db = pymysql.connect(host=HOST, user=USER, passwd=PASSWD, database=DATABASE)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `doctor` WHERE 1")
    result = cursor.fetchall()
    db.close()
    return result


def get_doctor_cabinet(doctor_id):
    db = pymysql.connect(host=HOST, user=USER, passwd=PASSWD, database=DATABASE)
    cursor = db.cursor()
    cursor.execute(f"SELECT DISTINCT cabinet.Cabinet_num FROM timetable_cabinet JOIN cabinet ON "
                   f"cabinet.Id = timetable_cabinet.Id_Cabinet WHERE timetable_cabinet.Id_Doctor = \"{doctor_id}\"")
    result = cursor.fetchone()
    db.close()
    return result


def get_worked_days_doctor(doctor_id):
    db = pymysql.connect(host=HOST, user=USER, passwd=PASSWD, database=DATABASE)
    cursor = db.cursor()
    cursor.execute("SELECT `Id_Doctor`, `Id_Day` FROM `timetable_cabinet` WHERE 1")
    result = cursor.fetchall()
    worked_days = list()
    for i in range(len(result)):
        if result[i][0] == doctor_id:
            worked_days.append(result[i][1] - 7)
    db.close()
    return worked_days


def get_time_work(doctor_id):
    db = pymysql.connect(host=HOST, user=USER, passwd=PASSWD, database=DATABASE)
    cursor = db.cursor()
    cursor.execute(f"SELECT time_work.Id_Work, time_work.Id_Time, time_interval.Id,  time_interval.Star, "
                   f"time_interval.End FROM time_work JOIN time_interval ON time_interval.Id = time_work.Id_Time "
                   f"WHERE time_work.Id_Work = \"{doctor_id}\"")
    result = cursor.fetchall()
    start_time = result[0][3]
    end_time = result[len(result) - 1][4]
    db.close()
    return start_time, end_time


def get_procedures():
    db = pymysql.connect(host=HOST, user=USER, passwd=PASSWD, database=DATABASE)
    cursor = db.cursor()
    cursor.execute("SELECT `Name_Service` FROM `service` WHERE 1")
    result = cursor.fetchall()
    db.close()
    return result


def get_procedures_cabinet():
    db = pymysql.connect(host=HOST, user=USER, passwd=PASSWD, database=DATABASE)
    cursor = db.cursor()
    cursor.execute("SELECT `Num_Cabinet` FROM `procedure_cabinet` WHERE 1")
    result = cursor.fetchall()
    db.close()
    return result


def get_days():
    db = pymysql.connect(host=HOST, user=USER, passwd=PASSWD, database=DATABASE)
    cursor = db.cursor()
    cursor.execute("SELECT `Day_num` FROM `days` WHERE 1")
    result = cursor.fetchall()
    db.close()
    return result


def get_id_day(day):
    db = pymysql.connect(host=HOST, user=USER, passwd=PASSWD, database=DATABASE)
    cursor = db.cursor()
    cursor.execute("SELECT `Id`, `Day_num` FROM `days` WHERE 1")
    result = cursor.fetchall()
    id_day = 7
    for i in range(len(result)):
        if result[i][1] == day:
            id_day = result[i][0]
            break
    db.close()
    return id_day


def get_time_interval():
    db = pymysql.connect(host=HOST, user=USER, passwd=PASSWD, database=DATABASE)
    cursor = db.cursor()
    cursor.execute("SELECT `Star`, `End` FROM `time_interval` WHERE 1")
    result = cursor.fetchall()
    db.close()
    return result


def get_days_for_procedure(id_procedure, id_cabinet):
    db = pymysql.connect(host=HOST, user=USER, passwd=PASSWD, database=DATABASE)
    cursor = db.cursor()
    cursor.execute(f"SELECT days.day_num, timetable_procedure.Id FROM timetable_procedure JOIN "
                   f"days ON days.Id = timetable_procedure.Id_Day WHERE timetable_procedure.Id_Name_Service "
                   f"= \"{id_procedure}\" AND timetable_procedure.Id_Cabinet_Procedure = \"{id_cabinet}\"")
    result = cursor.fetchall()
    db.close()
    return result


def get_registration_for_procedures(procedure, day):
    db = pymysql.connect(host=HOST, user=USER, passwd=PASSWD, database=DATABASE)
    cursor = db.cursor()
    cursor.execute("SELECT `Id_Procedure`, `Id_Day`, `Id_Time` FROM `time_work_procedure` WHERE 1")
    result = cursor.fetchall()
    data = []
    for i in range(len(result)):
        if result[i][0] == procedure and result[i][1] == day:
            data.append(result[i][2] - 8)
    db.close()
    return data


def add_entry_for_procedure(procedure, day, time, patient):
    db = pymysql.connect(host=HOST, user=USER, passwd=PASSWD, database=DATABASE)
    cursor = db.cursor()
    cursor.execute("SELECT `Id` FROM `time_work_procedure` WHERE 1")
    result = cursor.fetchall()
    new_id = result[len(result) - 1][0] + 1
    sql = f"INSERT INTO `time_work_procedure`(`Id`, `Id_Procedure`, `Id_Day`, `Id_Time`, `Id_Patient`) " \
          f"VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (int(new_id), int(procedure), int(day), int(time), int(patient)))
    db.commit()
    db.close()


def get_unique_procedure(login):
    db = pymysql.connect(host=HOST, user=USER, passwd=PASSWD, database=DATABASE)
    cursor = db.cursor()
    cursor.execute("SELECT `Id_Procedure`, `Id_Day`, `Id_Time`, `Id_Patient`, `Id` FROM `time_work_procedure` WHERE 1")
    result = cursor.fetchall()
    data = []
    for i in range(len(result)):
        if result[i][3] == login:
            data.append((result[i]))
    db.close()
    return data


def delete_procedure_entry(id_proc):
    db = pymysql.connect(host=HOST, user=USER, passwd=PASSWD, database=DATABASE)
    cursor = db.cursor()
    cursor.execute(f"DELETE FROM time_work_procedure WHERE id = {id_proc}")
    db.commit()
    db.close()
