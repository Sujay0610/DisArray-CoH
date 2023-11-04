import React, { useState } from 'react';
import axios from 'axios';

const CodeExecutor = () => {
  const [code, setCode] = useState('');
  const [output, setOutput] = useState('');
  const [error, setError] = useState('');

  const executeCode = async () => {
    try {
      const response = await axios.post('http://localhost:5000/execute', { code });
      setOutput(response.data.output);
      setError('');
    } catch (error) {
      setError(error.response ? error.response.data.error : 'Server error');
      setOutput('');
    }
  };

  return (
    <div>
      <textarea value={code} onChange={(e) => setCode(e.target.value)} />
      <button onClick={executeCode}>Execute</button>
      {output && <div>Output: {output}</div>}
      {error && <div>Error: {error}</div>}
    </div>
  );
};

export default CodeExecutor;
