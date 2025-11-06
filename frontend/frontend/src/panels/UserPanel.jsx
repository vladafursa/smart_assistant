import Message from "../components/Message";
import Form from "../components/Form";

const chatMessages = [{
  sender: "user",
  message: "message"
},
{
  sender: "assistant",
  message: "message"
}];

const chatMessageComponents = chatMessages.map((chatMessage)=>{
  return(
     <Message sender={chatMessage.sender} 
     text={chatMessage.message} />
  );
});

const UserPanel = ({ message }) => {
  return (
    <div className="flex flex-col h-full">
      {chatMessageComponents}
      <div className="mt-auto">
        <Form />
      </div>
    </div>
  );
};

export default UserPanel;
