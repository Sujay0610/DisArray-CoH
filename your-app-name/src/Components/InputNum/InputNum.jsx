import React from 'react'
import './InputNum.css'

const InputNum = () => {
  return (
    <div>
      <div className='inp'>
      <input type="text" name="username" placeholder="Enter your username"/>
      
        </div>
        <div className="inp-button">
            <button>Submit</button>
        </div>
    </div>
  )
}

export default InputNum
