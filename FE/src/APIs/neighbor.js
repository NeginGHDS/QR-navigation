const URL = `http://127.0.0.1:8000`;

export async function get_shotest_path_from_des_to_target_api(destination, target) {
    try {
        const response = await fetch(URL + `/neighbors/?current_node=${destination}&target_node=${target}`)
        if (response.ok) {
            const results = await response.json()
            return results
        } else {
            throw new Error("Application error ")
        }
    } catch (ex) {
        throw new Error("Network error " + ex)
    }
}


export async function get_neighbors_by_id(place_id, target_place) {
    try {
        const response = await fetch(URL + `/neighbors/${place_id}/${target_place}`)
        if (response.ok) {
            const results = await response.json()
            return results
        } else {
            throw new Error("Application error ")
        }
    } catch (ex) {
        throw new Error("Network error " + ex)
    }
}

export async function get_distance_between_neighbors_by_id(first_place_id, second_place_id) {
    try {
        const response = await fetch(URL + `/neighbors/distance/${first_place_id}/${second_place_id}`)
        if (response.ok) {
            const results = await response.json()
            return results
        } else {
            throw new Error("Application error ")
        }
    } catch (ex) {
        throw new Error("Network error " + ex)
    }
}