import React, { useEffect, useState } from 'react';
import io from 'socket.io-client';
import Header from '../../components/Header';
import Item from '../../components/Item';
import './styles.css';

export default function Main({ match }) {
    const [companys, setCompanys] = useState([]);

    useEffect(() => {
        const socket = io('http://localhost:3333', {
            query: { user: match.params.id}
        })

        socket.on('promotion', (msg) => {
            setCompanys(msg);
        });
    },[match.params.id]);

    console.log(companys)

    return (
        <div className="main-container">
            <Header />
            {/* <h1>IPromotion</h1>
            
            {companys.map(company => (
                <>
                <h2>{company.name}</h2>
                <h1 key={company._id}>{company.promotion}</h1>
                </>
            ))} */}
            <div className="box-container">
                {/* <Item name={"Company"} promotion={"Promotion"}/> */}
                {companys.map(company => (
                    <Item name={company.name} promotion={company.promotion}/>
                ))}
            </div>
        </div>
    );
}
