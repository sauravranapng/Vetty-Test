from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def display_file():
    try:
        
        target_file = request.args.get('file', 'file1.txt')

        
        start_line = int(request.args.get('start', 0))  
        end_line = int(request.args.get('end', -1))

        
        file_path = os.path.join(os.path.dirname(__file__), 'files', target_file)
        
        
        encodings = ['utf-8', 'utf-16', 'utf-16le', 'latin-1']

        content = None
        
        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as file:
                    lines = file.readlines()

                
                if end_line == -1:
                    end_line = len(lines)
                else:
                   
                    end_line += 1
                
               
                end_line = min(len(lines), end_line)

                
                content = ''.join(lines[start_line:end_line])
                break  
            except UnicodeDecodeError:
                continue 

        if content is None:
            raise ValueError("Unable to decode file with any of the tried encodings")

        
        return render_template('file_display.html', content=content)

    except Exception as e:
     
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
