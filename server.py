from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

saved_data = {}

@app.route('/')
def main_page():
    notes = None
    if 'note' in saved_data:
        notes = saved_data['note']
    edits = saved_data.setdefault('edit_count', 0)
    return render_template('index.html', notes=notes, edit_count=edits)


@app.route('/note', methods=['GET', 'POST'])
def note():
    if request.method == 'POST':
        saved_data['note'] = request.form
        saved_data['edit_count'] = saved_data.setdefault('edit_count', 0) + 1
        return redirect('/')
    return render_template('note.html')


if __name__ == '__main__':
    app.run(debug=True)