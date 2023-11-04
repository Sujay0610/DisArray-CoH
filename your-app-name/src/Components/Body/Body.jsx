import React from 'react';
import './Body.css';


const Body = () => {
  return (
    <div className="box">
    <div className="wrapper">
      <input type="checkbox" />
      <label>
        <i className='icon-off'>SOS</i>
      </label>
        <div className="add-number">
        <input
        type="text"
        id="phone"
        name="phone"
        placeholder="Enter a 10-digit phone number"
        pattern="^\d{10}$" 
      />
        </div>
    </div>
    </div>
  );
};

export default Body;

