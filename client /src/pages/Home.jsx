import React, { useEffect, useState } from 'react';
import CrimeList from '../components/CrimeList';
import { fetchCrimes } from '../services/api';

const Home = () => {
    const [crimes, setCrimes] = useState([]);

    useEffect(() => {
        const getCrimes = async () => {
            const data = await fetchCrimes();
            setCrimes(data);
        };
        getCrimes();
    }, []);

    return (
        <div>
            <h2>Crime Data</h2>
            <CrimeList crimes={crimes} />
        </div>
    );
};

export default Home;
