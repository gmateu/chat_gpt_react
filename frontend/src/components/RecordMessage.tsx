import {ReactMediaRecorder} from 'react-media-recorder'
import RecordIcon from './RecordIcon'

type Props = {
    handleStop: any;
}

function RecordMessage({handleStop}:Props) {
  return (
    <ReactMediaRecorder 
        audio
        onStop={handleStop}
        render={({status,startRecording,stopRecording})=>{
            <div className='mt-2'>djslsdj</div>
        }}
    />

  )
}

export default RecordMessage