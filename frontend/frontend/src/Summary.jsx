import './index.css'; 

const SummaryBox = ({ text }) => {
  return (
    <div className="summary-container">
      <label className="summary-label">Summary</label>
      <div className="summary-box">
        {text || 'there will be summary'}
      </div>
    </div>
  );
};

export default SummaryBox;