import { useState } from "react";
import Navbar from "./components/Navbar";
import Search from "./components/Search";
import Result from "./components/Result";
import Stats from "./components/Stats";

function App() {
  const [result, setResult] = useState(null);

  const handleSearch = async (query) => {
    const start = performance.now();
    const res = await fetch(`http://127.0.0.1:8000/data?q=${query}`);
    const data = await res.json();
    const end = performance.now();

    setResult({
      ...data,
      time: Math.round(end - start)
    });
  };

  return (
    <>
      <Navbar />
      <Search onSearch={handleSearch} />
      <Result result={result} />
      <Stats />
    </>
  );
}

export default App;
