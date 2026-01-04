import {useState} from "react";

export default function Search({onSearch}) {
    const [query, setQuery] = useState("");

    return (
        <div>
            <input
            value={query}
            onChange={(e)=> setQuery(e.target.value)}
            placeholder="Enter search query"
            />
            <button onClick={() => onSearch (query)}>Fetch Data</button>

        </div>
    );
}