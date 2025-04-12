import React from 'react';

const CrimeList = ({ crimes }) => {
    return (
        <ul>
            {crimes.map((crime) => (
                <li key={crime.id}>{crime.description} - {crime.date}</li>
            ))}
        </ul>
    );
};

export default CrimeList;
