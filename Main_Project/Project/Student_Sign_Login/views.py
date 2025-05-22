import mysql.connector
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
 
 
def unified_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        login_type = request.POST.get('login_type')
 
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Prav@1234567",
                database="student_management"
            )
            cursor = conn.cursor()
 
            if login_type == 'student':
                query = "SELECT * FROM student WHERE `username`=%s AND `pwd`=%s"
                cursor.execute(query, (username, password))
                result = cursor.fetchone()
                if result:
                    request.session['student'] = username
                    return redirect('student_dashboard')
 
            elif login_type == 'faculty':
                query = "SELECT * FROM faculty WHERE `username`=%s AND `pwd`=%s"
                cursor.execute(query, (username, password))
                result = cursor.fetchone()
                if result:
                    request.session['faculty'] = username
                    return redirect('faculty_dashboard')
 
            elif login_type == 'parent':
                query = "SELECT * FROM parent WHERE `username`=%s AND `pwd`=%s"
                cursor.execute(query, (username, password))
                result = cursor.fetchone()
                if result:
                    request.session['parent'] = username
                    return redirect('parent_dashboard')
 
            messages.error(request, 'Invalid credentials or login type.')
 
        except mysql.connector.Error as err:
            messages.error(request, f"Database error: {err}")
        finally:
            cursor.close()
            conn.close()
 
    return render(request, 'unified_login.html')
 
 
def student_dashboard(request):
    username = request.session.get('student')
    if not username:
        return redirect('unified_login')
 
    try:
        # Connect to MySQL database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Prav@1234567",
            database="student_management"
        )
        cursor = conn.cursor(dictionary=True)
 
        # Fetch student details
        query = "SELECT student_id, name FROM student WHERE username = %s"
        cursor.execute(query, (username,))
        student = cursor.fetchone()
    except mysql.connector.Error as err:
        student = None
        print(f"Database error: {err}")
    finally:
        cursor.close()
        conn.close()
 
    return render(request, 'student_dashboard.html', {
        'username': student['s_name'] if student and 's_name' in student else 'Guest',
        's_id': student['id'] if student and 'id' in student else 'N/A',
    })
   
 
 
def faculty_dashboard(request):
    username = request.session.get('faculty', 'Guest')
    return render(request, 'faculty_dashboard.html', {'username': username})
 
 
def parent_dashboard(request):
    username = request.session.get('parent', 'Guest')
    return render(request, 'parent_dashboard.html', {'username': username})
 