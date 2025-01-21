from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # セッション用キー

# 認証情報
VALID_CREDENTIALS = {
    'メールアドレス': '111',  # ID
    'パスワード': '222'       # パスワード
}

@app.route('/')
def index():
    """ログイン画面を表示"""
    if session.get('logged_in'):
        return redirect(url_for('page1'))
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    """ログイン処理"""
    mail = request.form.get('mail')
    password = request.form.get('password')
    
    if mail == VALID_CREDENTIALS['メールアドレス'] and password == VALID_CREDENTIALS['パスワード']:
        session['logged_in'] = True
        return redirect(url_for('page1'))
    
    return render_template('login.html', error="メールアドレスまたはパスワードが正しくありません")

@app.route('/page1')
def page1():
    """ページ1表示"""
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    return render_template('page1.html')

@app.route('/page2', methods=['GET', 'POST'])
def page2():
    """ページ2表示"""
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        # フォームデータを取得
        name = request.form.get('member_secret_answer')
        return render_template('page2.html', name=name)
    
    return render_template('page2.html')

@app.route('/page3')
def page3():
    """ページ3表示"""
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    return render_template('page3.html')

@app.route('/page4')
def page4():
    """ページ4表示"""
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    return render_template('page4.html')

@app.route('/page5')
def page5():
    """ページ5表示"""
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    return render_template('page5.html')

@app.route('/logout')
def logout():
    """ログアウト処理"""
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
