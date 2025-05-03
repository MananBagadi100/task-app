import { useState } from "react";
import { useNavigate } from "react-router-dom";
import useAuth from "../hooks/useAuth";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [err, setErr] = useState("");
  const { login } = useAuth();
  const nav = useNavigate();

  const submit = async (e) => {
    e.preventDefault();
    try {
      await login(email, password);
      nav("/dashboard");
    } catch {
      setErr("Invalid credentials");
    }
  };

  return (
    <div className="h-screen flex items-center justify-center">
      <form onSubmit={submit} className="w-80 space-y-4">
        <h1 className="text-2xl font-semibold text-center">Login</h1>
        <input className="input" placeholder="Email" value={email}
               onChange={(e) => setEmail(e.target.value)} />
        <input className="input" type="password" placeholder="Password" value={password}
               onChange={(e) => setPassword(e.target.value)} />
        {err && <p className="text-red-500">{err}</p>}
        <button className="btn w-full">Sign in</button>
      </form>
    </div>
  );
}
