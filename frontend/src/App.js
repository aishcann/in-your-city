
import './app.scss';
import HomePage from './components/HomePage/HomePage';
import LoginPage from './components/LoginPage/LoginPage';
import ManageEvents from './components/ManageEvents/ManageEvents'

function App() {
  return (
    <div className="App">
        <HomePage/>
        <LoginPage/>
        <ManageEvents/>
    </div>
  );
}

export default App;
