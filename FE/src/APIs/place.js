const URL = `http://127.0.0.1:8000`;

export async function get_all_places_api() {
    try {
        const response = await fetch(URL + `/places`)
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