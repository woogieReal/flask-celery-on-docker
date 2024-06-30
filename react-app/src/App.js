import './App.css';
import { useEffect, useState } from 'react';

function App() {
  const [logs, setLogs] = useState([]);

  function getRandomInt() {
    return Math.floor(Math.random() * 100) + 1;
  }

  function getRandomOperator() {
    const operators = ['+', '-', '*', '/'];
    const randomIndex = Math.floor(Math.random() * operators.length);
    return operators[randomIndex];
  }

  const getApiLogs = async () => {
    const response = await fetch('http://localhost:5000/api_logs');
    const data = await response.json();
    setLogs(data);
  }

  function calculate(num1, num2, operator) {
    let result;

    switch (operator) {
      case '+': result = num1 + num2; break;
      case '-': result = num1 - num2; break;
      case '*': result = num1 * num2; break;
      case '/': result = num1 / num2; break;
      default: result = 'Invalid operator';
    }

    return {
      expression: `${num1} ${operator} ${num2}`,
      result,
    };
  }

  const postApiLogs = async () => {
    const num1 = getRandomInt();
    const num2 = getRandomInt();
    const operator = getRandomOperator();
    const { expression, result } = calculate(num1, num2, operator);

    await fetch('http://localhost:5000/add_to_queue', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        "apiRequest": expression,
        "apiResponse": result
      })
    });
    await getApiLogs();
  }

  useEffect(() => {
    getApiLogs();
  }, [])

  return (
    <div className="App">
      <div className="App-body">
        <button onClick={postApiLogs} style={{ width: 500, height: 100, fontSize: 50 }}>POST_API_LOGS</button>
        <table>
          <thead>
            <tr>
              <th>LOG_ID</th>
              <th>API_REQUEST</th>
              <th>API_RESPONSE</th>
              <th>CREATION_DATE</th>
            </tr>
          </thead>
          <tbody>
            {logs.map((log, idx) => (
              <tr key={idx}>
                <td>{log.logId}</td>
                <td>{log.apiRequest}</td>
                <td>{log.apiResponse}</td>
                <td>{log.creationDate}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default App;
