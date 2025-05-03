import { useState } from "react";
import api from "../api/axios";

export default function useAuth() {
  const [token, setToken] = useState(() => localStorage.getItem("token"));

  const login = async (email, password) => {
    const res = await api.post("/auth/login", { email, password });
    localStorage.setItem("token", res.data.token);
    setToken(res.data.token);
  };

  const logout = () => {
    localStorage.removeItem("token");
    setToken(null);
  };

  return { token, login, logout };
}
