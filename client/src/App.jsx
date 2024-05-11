import axios from 'axios'
import './App.css'
import { useEffect, useState } from 'react'

const dataTobeSent = {
  name: 'Fame',
}

function App() {
  const [count, setcount] = useState(false)
  useEffect(() => {
    if (count){
      axios.post('http://localhost:8080/postdata', dataTobeSent).then(response => console.log(response)).catch(error => console.log(error))
      console.log('works')
    }
  }, [count])
  return (
    <>
      <div>
          <button onClick={() => setcount(true)}>Click</button>
      </div>
    </>
  )
}

export default App
