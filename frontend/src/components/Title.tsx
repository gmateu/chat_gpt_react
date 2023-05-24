import { useState} from 'react'
import axios from 'axios'

type Props = {
    setMessages: any;
}


function Title({ setMessages }: Props) {
    const [isResetting,setIsResetting] = useState(false)

    //reset conversation
    const resetConversation = async () => {
        console.log('Resetting')
        setIsResetting(true)
        await axios.get("http://192.168.1.10:8000/reset").then((res) => {
            if(res.status==200){
                setMessages([])
            }else{
                console.error("error with api request")
            }
        })
        .catch((err)=>{
            console.error(err.message)
        })
        setIsResetting(false)
    }
  return (
    <div>
        <button onClick={resetConversation} className='bg-indigo-500 p-5'>reset</button>
    </div>
  )
}

export default Title