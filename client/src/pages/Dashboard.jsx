import { useEffect, useState } from "react";
import api from "../api/axios";
import TaskRow from "../components/TaskRow";
import TaskForm from "./TaskForm";

export default function Dashboard() {
  const [tasks, setTasks] = useState([]);
  const [filter, setFilter] = useState("All");
  const [showForm, setShowForm] = useState(false);

  useEffect(() => {
    api.get("/tasks/").then((r) => setTasks(r.data));
  }, []);

  const addTask = (newTask) => setTasks((t) => [...t, newTask]);

  const toggle = async (task) => {
    const res = await api.put(`/tasks/${task.id}`, {
      status: task.status === "complete" ? "incomplete" : "complete",
    });
    setTasks((t) => t.map((x) => (x.id === task.id ? res.data : x)));
  };

  const remove = async (id) => {
    await api.delete(`/tasks/${id}`);
    setTasks((t) => t.filter((x) => x.id !== id));
  };

  const visible = tasks.filter((t) =>
    filter === "All"
      ? true
      : filter === "Completed"
      ? t.status === "complete"
      : t.status !== "complete"
  );

  return (
    <div className="max-w-xl mx-auto py-8">
      <div className="flex justify-between items-center mb-4">
        <h1 className="text-3xl">My Tasks</h1>
        <button className="btn" onClick={() => setShowForm(true)}>
          + Add
        </button>
      </div>

      <div className="flex gap-2 mb-4">
        {["All", "Active", "Completed"].map((f) => (
          <button
            key={f}
            className={`px-3 py-1 rounded ${
              filter === f ? "bg-blue-600 text-white" : "border"
            }`}
            onClick={() => setFilter(f)}
          >
            {f}
          </button>
        ))}
      </div>

      <ul className="space-y-2">
        {visible.map((t) => (
          <TaskRow key={t.id} task={t} onToggle={toggle} onDelete={remove} />
        ))}
      </ul>

      {showForm && <TaskForm close={() => setShowForm(false)} onSave={addTask} />}
    </div>
  );
}
