import React from "react";
import { Button } from "@/components/ui/button";

const ValetParkingApp = () => {
  return (
    <div className="min-h-screen bg-white flex flex-col items-center justify-center p-6">
      <h1 className="text-3xl font-bold text-gray-900 mb-6">Recogida de Vehículos</h1>
      <p className="text-lg text-gray-700 mb-4 text-center max-w-md">
        Consulta los vehículos disponibles para recoger y gestiona la entrega de manera eficiente.
      </p>
      <div className="w-full max-w-2xl bg-gray-100 p-4 rounded-xl shadow-md">
        <h2 className="text-xl font-semibold text-gray-900 mb-4">Vehículos en Espera</h2>
        <ul className="space-y-3">
          <li className="p-3 bg-white rounded-lg shadow flex justify-between items-center">
            <span className="text-gray-800">Toyota Corolla - ABC123</span>
            <Button className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">
              Entregar
            </Button>
          </li>
          <li className="p-3 bg-white rounded-lg shadow flex justify-between items-center">
            <span className="text-gray-800">Honda Civic - XYZ789</span>
            <Button className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">
              Entregar
            </Button>
          </li>
        </ul>
      </div>
    </div>
  );
};

export default ValetParkingApp;
