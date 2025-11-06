import Message from "../components/Message";
import Form from "../components/Form";
import { useEffect, useState } from "react";

const UserPanel = ({ message }) => {
  const [chatMessages, setChatMessages] = useState([
    { sender: "assistant", message: "Hello! How can I help you?" }
  ]);
  const handleSend = (text, sender) => {
  setChatMessages((prev) => [...prev, { sender, message: text }]);
  };

  return (
    <div className="flex flex-col h-full">
       {chatMessages.map((chatMessage, i) => (
          <Message key={i} sender={chatMessage.sender} text={chatMessage.message} />
        ))}
      <div className="mt-auto">
        <Form sender="user" onSend={(text) => handleSend(text, "user")} />
      </div>
    </div>
  );
};

export default UserPanel;
