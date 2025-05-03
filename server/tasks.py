from flask import Blueprint
tasks_bp = Blueprint('tasks', __name__)
from flask import request, jsonify
from .models import Task,User,db
from .utils import token_required

# GET all tasks
@tasks_bp.route('/', methods=['GET'])
@token_required
def get_tasks(current_user):
    status_filter = request.args.get('status')  # ?status=complete
    query = Task.query.filter_by(user_id=current_user.id)
    if status_filter:
        query = query.filter_by(status=status_filter)
    tasks = query.all()
    return jsonify([{
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'status': task.status,
        'priority': task.priority,
        'created_at': task.created_at.isoformat()
    } for task in tasks]), 200

# CREATE task
@tasks_bp.route('/', methods=['POST'])
@token_required
def create_task(current_user):
    data = request.get_json()
    new_task = Task(
        title       = data['title'],
        description = data.get('description', ''),
        status      = 'incomplete',
        priority    = data.get('priority', 'Low'),
        user_id     = current_user.id
    )
    db.session.add(new_task)
    db.session.commit()

    # Return the newly‐created task object, not just a message:
    return jsonify({
        'id':          new_task.id,
        'title':       new_task.title,
        'description': new_task.description,
        'status':      new_task.status,
        'priority':    new_task.priority,
        'created_at':  new_task.created_at.isoformat(),
        'user_id':     new_task.user_id
    }), 201



# UPDATE task
@tasks_bp.route('/<int:task_id>', methods=['PUT'])
@token_required
def update_task(current_user, task_id):
    task = Task.query.get(task_id)
    if not task or task.user_id != current_user.id:
        return jsonify({ 'message': 'Task not found' }), 404

    data = request.get_json()
    task.title       = data.get('title',       task.title)
    task.description = data.get('description', task.description)
    task.status      = data.get('status',      task.status)
    task.priority    = data.get('priority',    task.priority)
    db.session.commit()

    # Return the updated record
    return jsonify({
        'id':          task.id,
        'title':       task.title,
        'description': task.description,
        'status':      task.status,
        'priority':    task.priority,
        'created_at':  task.created_at.isoformat(),
        'user_id':     task.user_id
    }), 200

# DELETE task
@tasks_bp.route('/<int:task_id>', methods=['DELETE'])
@token_required
def delete_task(current_user, task_id):
    task = Task.query.get(task_id)
    if not task or task.user_id != current_user.id:
        return jsonify({'message': 'Task not found'}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted'}), 200
