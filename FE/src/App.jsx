import '@mantine/core/styles.css';
import './App.css'
import { MantineProvider } from '@mantine/core';
import  Main  from './components/main'

function App() {
  return <MantineProvider><Main/></MantineProvider>;
  
}

export default App
