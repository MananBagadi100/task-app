import { useState } from "react";
import api from "../api/axios";

export default function TaskForm({ close, onSave }) {
  const [title, setTitle] = useState("");
  const [priority, setPriority] = useState("Low");

  const submit = async (e) => {
    e.preventDefault();
    /* const res = await api.post("/tasks/", { title, priority });
    onSave(res.data);
    close(); */
    try {
        const res=await api.post("/tasks/",{title,priority});
        onSave(res.data);
        close();

    }
    catch(err) {
        console.error(err);
        alert("Could not save task");
    }
  };

  return (
    <div className="fixed inset-0 bg-black/30 flex items-center justify-center">
      <form onSubmit={submit} className="bg-white p-6 rounded space-y-4 w-80">
        <h2 className="text-xl font-semibold">New task</h2>
        <input className="input" placeholder="Title" value={title}
               onChange={(e) => setTitle(e.target.value)} required />
        <select className="input" value={priority}
                onChange={(e) => setPriority(e.target.value)}>
          {["Low", "Medium", "High"].map((p) => (
            <option key={p}>{p}</option>
          ))}
        </select>
        <div className="flex justify-end gap-2">
          <button type="button" className="btn bg-gray-300 text-black"
                  onClick={close}>Cancel</button>
          <button className="btn">Save</button>
        </div>
      </form>
    </div>
  );
}
