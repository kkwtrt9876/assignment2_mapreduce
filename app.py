from flask import Flask, request, redirect, url_for, render_template, flash
import os
import subprocess

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd()
data_1 = 11

@app.route('/')
def index():
    return render_template('index.html')

def run_mapreduce_job(input_path1, input_path2, output_path, mapper_path, reducer_path):
    # Run the MapReduce job
    cmd = [
        "hadoop",
        "jar",
        "/usr/local/hadoop-2.10.2/share/hadoop/tools/lib/hadoop-streaming-2.10.2.jar",
        "-input", input_path1,
        "-input", input_path2,
        "-output", output_path,
        "-mapper", "mapper.py",
        "-reducer", "reducer.py",
        "-file", mapper_path,
        "-file", reducer_path
    ]
    subprocess.run(cmd)

def get_output(output_path):
    cmd = [
        "hadoop",
        "fs",
        "-cat",
        os.path.join(output_path, "part-00000")
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

def upload_file1(upload_path):
    # Run the MapReduce job
    cmd = [
        "hadoop",
        "fs",
        "-put",
        upload_path,
        "/inputs/",
    ]
    subprocess.run(cmd)

@app.route('/upload', methods=['POST'])
def upload_file():
    global data_1
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and file.filename.endswith('.txt'):
        data_1 += 1
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        input_path1 = "/inputs/"+file.filename
        input_path2 = "/inputs/output1/part-00000"
        mapper_path = "/home/i221944/map_reduced_project/mapper.py"
        reducer_path = "/home/i221944/map_reduced_project/reducer.py"
        output_path = f"/inputs/output{data_1}"
        upload_file1(file_path)
        
        run_mapreduce_job(input_path1, input_path2, output_path, mapper_path, reducer_path)
        output = get_output(output_path)
        return render_template('result.html', output=output)
    else:
        flash('Invalid file type. Only .txt files are allowed.')
        return redirect(request.url)

if __name__ == '__main__':
    app.secret_key = 'supersecretkey'
    app.run(debug=True)
