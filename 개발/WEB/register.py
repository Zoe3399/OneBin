from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL 데이터베이스 연결 설정
db = mysql.connector.connect(
    host='project-db-stu3.smhrd.com',
    user='Insa4_IOTA_hacksim_5',
    passwd='aishcool5',
    db='Insa4_IOTA_hacksim_5',
    port=3307
)

def is_duplicate_id(admin_id):
    cursor = db.cursor()
    sql = "SELECT COUNT(*) FROM admin WHERE ADMIN_ID = %s"
    cursor.execute(sql, (admin_id,))
    count = cursor.fetchone()[0]
    cursor.close()
    return count > 0

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        admin_id = request.form['ADMIN_ID']
        admin_pw = request.form['ADMIN_PW']
        company = request.form['COMPANY']
        ph = request.form['PH']

        if is_duplicate_id(admin_id):
            return "이미 사용 중인 아이디입니다."

        cursor = db.cursor()
        sql = "INSERT INTO admin (ADMIN_ID, ADMIN_PW, COMPANY, PH) VALUES (%s, %s, %s, %s)"
        values = (admin_id, admin_pw, company, int(ph))

        cursor.execute(sql, values)
        db.commit()
        cursor.close()

        return "회원가입이 성공적으로 완료되었습니다."
    


@app.route('/check_id_duplicate/<admin_id>')
def check_id_duplicate(admin_id):
    cursor = db.cursor()
    sql = "SELECT COUNT(*) FROM admin WHERE ADMIN_ID = %s"
    cursor.execute(sql, (admin_id,))
    count = cursor.fetchone()[0]
    cursor.close()

    if count > 0:
        return "duplicate"
    else:
        return "not_duplicate"

if __name__ == '__main__':
    app.run(debug=True)