const URL = `http://127.0.0.1:8000`;

export async function interact_with_agent(destination, departure, shortest_path, traversed_places, places_in_shortest_path, current_place) {
    const payload = {"destination":destination, "departure":departure, "shortest_paths": shortest_path , "traversed_places": traversed_places, "places_in_shortest_path":places_in_shortest_path, "current_place":current_place}
    // console.log(payload)
    const response = await fetch(URL + `/agent/call`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    })
    if (!response.ok) {
        let errMessage = await response.json();
        if (response.status === 422)
            errMessage = `${errMessage.errors[0].msg} for ${errMessage.errors[0].path}.`
        else
            errMessage = errMessage.error;
        throw errMessage;
    }
    else{
        const agent_response = await response.json();
        return agent_response
    } ;
}