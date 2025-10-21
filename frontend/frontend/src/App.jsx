import Header from './Header.jsx'
import SummaryBox from './Summary.jsx';
function App() {
    const summaryText = "There will be summary";
return ( 
    <div>
    <Header></Header>
      <SummaryBox text={summaryText} />
    </div>
)
}

export default App
