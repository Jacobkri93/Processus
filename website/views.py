from flask import Blueprint, render_template, request, flash, jsonify, Flask
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os
from .models import Note, File
from . import db
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/file_site', methods=['GET','POST'])
@login_required
def file_site():
    # Retrieve the file object from the request
    # file = request.files.get('file')
    # if file:
    #     # Read the file contents
    #     file_contents = file.read()

    #     # Create a new File record
    #     record = File(name=file.filename, data=file_contents)

    #     # Save the record to the database
        
    #     db.session.add(record)
    #     db.session.commit()
        return render_template("file_site.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
