import {useEffect,useState} from "react";
export default function Stats() {
const[stats,setStats]=useState(null);

useEffect(()=>{
    fetch("http://127.0.0.1:8000/cache/stats")
    .then((res)=>res.json())
    .then((data)=>setStats(data));
},[]);
if(!stats)return null;

return (
    <div>
        <h3>Cache Statistics</h3>
        <p><b>Cache Size:</b> {stats.capacity}</p>
        <p><b>Current Size:</b> {stats.current_size}</p>
        <p><b>Hit Count:</b> {stats.hits}</p>
        <p><b>Miss Count:</b> {stats.misses}</p>
    </div>
);
}
