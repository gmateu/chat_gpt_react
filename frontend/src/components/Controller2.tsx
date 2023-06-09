import React from 'react'
import { ReactMediaRecorder } from "react-media-recorder";

//rfce
const Controller2= () => {
    return (
      <ReactMediaRecorder 
        screen

        render={({status,startRecording,stopRecording,mediaBlobUrl})=>(
          <div>
            <p>{status}</p>
            <button className='bg-blue-200 p-5' onClick={startRecording}>start</button>
            <button className='bg-red-200 p-5' onClick={stopRecording}>stop</button>
            <video src={mediaBlobUrl} autoPlay loop controls></video>

          </div>
    )}
      
      />
    );
  };

export default Controller2