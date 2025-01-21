from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# 認証情報を変更
VALID_CREDENTIALS = {
    'メールアドレス': '111',  # ID
    'パスワード': '222'       # パスワード
}

@app.route('/')
def index():
    # ログイン画面の表示
    return render_template('login.html')  # 必ず login.html を templates フォルダに配置

@app.route('/login', methods=['POST'])
def login():
    # フォームからデータ取得
    mail = request.form.get('mail')
    password = request.form.get('password')
    
    # 認証チェック
    if mail == VALID_CREDENTIALS['メールアドレス'] and password == VALID_CREDENTIALS['パスワード']:
        session['logged_in'] = True
        return redirect(url_for('page1'))  # ログイン成功時、page1 へリダイレクト
    
    # ログイン失敗時エラーメッセージを渡して再表示
    return render_template('login.html', error="メールアドレスまたはパスワードが正しくありません")

@app.route('/page1')
def page1():
    # セッション認証の確認
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    return render_template('page1.html')  # 必ず page1.html を templates フォルダに配置

@app.route('/page2')
def page2():
    # セッション認証の確認
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    return render_template('page2.html')  # 必ず page2.html を templates フォルダに配置

@app.route('/page3')
def page3():
    # セッション認証の確認
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    return render_template('page3.html')  # 必ず page3.html を templates フォルダに配置

@app.route('/page4')
def page4():
    # セッション認証の確認
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    return render_template('page4.html')  # 必ず page4.html を templates フォルダに配置

@app.route('/page5')
def page5():
    # セッション認証の確認
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    return render_template('page5.html')  # 必ず page5.html を templates フォルダに配置

@app.route('/logout')
def logout():
    # ログアウト時にセッションをクリア
    session.clear()
    return redirect(url_for('index'))  # ログイン画面へ戻る

if __name__ == '__main__':
    # アプリケーションを起動
    app.run(debug=True, host='0.0.0.0', port=8080)
