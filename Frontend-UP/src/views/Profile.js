import React, { useEffect, useState } from "react";

const Profile = () => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/user/1")  // Ajusta el endpoint según tu API
      .then((response) => response.json())
      .then((data) => setUser(data))
      .catch((error) => console.error("Error al obtener el usuario:", error));
  }, []);

  if (!user) return <p className="text-center">Cargando perfil...</p>;

  return (
    <div className="flex flex-col items-center p-6 bg-gray-100 min-h-screen">
      <div className="bg-white p-6 rounded-2xl shadow-lg w-full max-w-md text-center">
        <img
          src={user.foto_perfil}
          alt="Foto de perfil"
          className="w-32 h-32 rounded-full mx-auto mb-4"
        />
        <h2 className="text-xl font-bold">{user.nombre}</h2>
        <p className="text-gray-500">{user.email}</p>
        <p className="text-gray-700 mt-2"><strong>Rol:</strong> {user.rol}</p>
        <p className="text-gray-700"><strong>Teléfono:</strong> {user.teléfono}</p>
      </div>
    </div>
  );
};

export default Profile;
