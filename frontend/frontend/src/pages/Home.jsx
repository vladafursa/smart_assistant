import Header from '../components/Header.jsx'
import AssistantPanel from '../panels/AssistantPanel.jsx';
import UserPanel from '../panels/UserPanel.jsx';

function Home() {
    const summaryText = "There will be summary";
return ( 
    <div className="h-screen flex flex-col bg-neutral-50">
        <div className='sticky top-0'>
        <Header />
        </div>
      <div className="flex flex-1">
        <div className="flex-[0.4] border-r p-4">
          <UserPanel message="message" />
        </div>
        
        <div className="flex-[0.6] p-4">
          <AssistantPanel summary_text={summaryText} />
        </div>
      </div>
    </div>
)
}

export default Home
