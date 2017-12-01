<!DOCTYPE html> 
def rotate_string(text, rot): 
    rotated = '' 
    for char in text: 
       if (char.isalpha()): 
           rotated = rotated + rotate_character(char, rot) 
       else: 
           rotated = rotated + char 


   return rotated

@app.route("/customer_id", methods=['POST'])
def customer_id():
    first_name = request.form['first_name']
    
    return render_template('hello_greeting.html', name=first_name) 
<html> 
    
    <body> 
        
        <!-- Auto generating customer-id using "first name" by  caesar --> 
        <form method='POST'>
        <label for="rot">
                Rotate by:
                <input name="rot" value="0" type="text" />
        </label>
        
        <br>
        
        <textarea type="text" value="0" name="text">{0}</textarea>
        
        <br>
        <input type="Submit" />
        </form>

    </body> 
</html> 