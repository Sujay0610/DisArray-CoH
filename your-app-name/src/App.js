import logo from './logo.svg';
import './App.css';
import CodeExecutor from './Components/Code/codexec';
import Navbar from './Components/Navbar/Navbar';
import Body from './Components/Body/Body';
import InputNum from './Components/InputNum/InputNum';

function App() {
  return (
    <div className="App">
      <Navbar/>
      <Body/>
      <InputNum/>
    </div>
  );
}

export default App;
