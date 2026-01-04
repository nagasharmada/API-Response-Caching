export default function Result({ result }){
    if(!result)return null;
    return(
        <div>
            <p><b>Source: </b> {result.source}</p>
            <p><b>Query: </b> {result.data.query}</p>
            <p><b>Result: </b>{result.data.result}</p>
        </div>   );
}