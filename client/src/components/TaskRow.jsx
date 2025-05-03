import PropTypes from "prop-types";

export default function TaskRow({ task, onToggle, onDelete }) {
    return (
        <li className="flex items-center justify-between p-3 mb-2 border rounded hover:shadow-sm">
          {/*for displaying the  left side: checkbox and text */}
          <div className="flex items-start space-x-3">
            <input
              type="checkbox"
              checked={task.status === "complete"}
              onChange={() => onToggle(task)}
              className="mt-1 h-4 w-4"
            />
            <div>
              <div className="text-lg font-medium">{task.title}</div>
              <div className="mt-1 inline-block text-xs font-semibold text-gray-600 bg-gray-100 px-2 py-0.5 rounded">
                Priority: {task.priority}
              </div>
            </div>
          </div>
    
          {/* right side: delete button */}
          <button
            onClick={() => onDelete(task.id)}
            className="text-gray-500 hover:text-red-600"
            aria-label="Delete task"
          >
            🗑️
          </button>
        </li>
    );
}

TaskRow.propTypes = {
  task: PropTypes.object.isRequired,
  onToggle: PropTypes.func.isRequired,
  onDelete: PropTypes.func.isRequired,
};
