import Message from "../components/Message";
import Form from "../components/Form";

const UserPanel = ({ message }) => {
  return (
    <div className="flex flex-col h-full">
      <Message sender="user" text={message} />

      <div className="mt-auto">
        <Form />
      </div>
    </div>
  );
};

export default UserPanel;
