import { NavLink, useLocation } from "react-router-dom";
import { FaRegFileAlt } from "react-icons/fa"; // документ
import { FaHome } from "react-icons/fa";       // домик

const Header = () => {
  const location = useLocation();

  const isOnStorage = location.pathname === "/storage";

  return (
    <header className="bg-purple-400 text-white px-6 py-3 shadow flex items-center justify-between">
      <h1 className="text-lg font-semibold">Support Assistant</h1>
      {isOnStorage ? (
        <NavLink to="/" end>
          <FaHome className="text-2xl cursor-pointer hover:text-purple-200" />
        </NavLink>
      ) : (
        <NavLink to="/storage" end>
          <FaRegFileAlt className="text-2xl cursor-pointer hover:text-purple-200" />
        </NavLink>
      )}
    </header>
  );
};

export default Header;
