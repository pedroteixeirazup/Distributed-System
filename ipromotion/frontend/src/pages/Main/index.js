import React, { useEffect } from 'react';
import io from 'socket.io-client';

export default function Main({ match }) {
    useEffect(() => {
        const socket = io('http://localhost:3333', {
            query: { user: match.params.id}
        })

        socket.emit('client message','alo')
        socket.on('promotion', (person) => {
            console.log('His name is ' + person.name)
        });
    });

    return (
        <div className="main-container">
            <h1>Alou</h1>
        </div>
    );
}
