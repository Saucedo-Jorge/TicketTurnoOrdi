import { useState } from 'preact/hooks';


export default function Greeting({messages, session}) {

  const randomMessage = () => messages[(Math.floor(Math.random() * messages.length))];

  const [greeting, setGreeting] = useState(randomMessage());

  return (
    <div>
      {
       session ? (
        <>
           <h3>{greeting} ¡Gracias por tu visita {session.user?.name}!</h3>
        </>
      ) : (
        <>
          <h3>{greeting} ¡Gracias por tu visita!</h3>
        </>
      )
      }
      <button onClick={() => setGreeting(randomMessage())}>
        Nuevo saludo
      </button>
    </div>
  );
}