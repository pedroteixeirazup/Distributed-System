import React from 'react';
import './styles.css';
// import { Container } from './styles';

export default function Item({name, promotion}) {
  return (
    <div className="main-container">
        <span>
            <strong>
                {name}
            </strong>
            <p>
                {promotion}
            </p>
        </span>
    </div>
  );
}
