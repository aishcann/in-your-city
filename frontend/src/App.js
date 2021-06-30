import HomePage from './components/HomePage/HomePage';
import EventDetail from './components/EventDetail/EventDetail';
import LoginPage from './components/LoginPage/LoginPage';
import ManageEvents from './components/ManageEvents/ManageEvents';

const App = () => {
  return (
    <div className="app">
     hello from app
     <HomePage/>
     <EventDetail/>
     <LoginPage/>
     <ManageEvents/>
    </div>
  );
}

export default App;
