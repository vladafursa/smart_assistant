import SummaryBox from '../components/Summary.jsx';
import Form from '../components/Form.jsx';

const AssistantPanel = ({ summary_text }) => {
  return (
    <div className="flex flex-col h-full">
     
      <SummaryBox text={summary_text} />

      <div className="mt-auto">
        <Form />
      </div>
    </div>
  );
};

export default AssistantPanel;
