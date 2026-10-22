import { Select, Group, Button, Stack, Text } from '@mantine/core';
import { get_shotest_path_from_des_to_target_api, get_distance_between_neighbors_by_id } from '../../APIs/neighbor';
import { Link } from "react-router-dom";
function Init({ traversed, setRoadMap, setTraversed, places, departure, setDeparture, destination, setDestination, setDistance }) {
    // console.log(places)

    // console.log(departure)


    const mapPlacesToSelectData = (places) => {
      const groups = {};
    
      places.forEach(place => {
        const section = place.section || "Other";
    
        if (!groups[section]) {
          groups[section] = [];
        }
    
        groups[section].push({
          value: String(place.place_id), // Select value
          label: place.name,        // Display text
        });
      });

      // console.log(groups)
    
      return Object.entries(groups).map(([group, items]) => ({
        group,
        items,
      }));
    };

    const selectData = mapPlacesToSelectData(places);



    const depature_select_handler = (place_id)=>{
      const selected = places.find(
        place => place.place_id === place_id
      );
      // console.log(selected)
      setDeparture(selected ?? {});
      // console.log(departure)
    }
    const destination_select_handler = (place_id)=>{
      const selected = places.find(
        place => place.place_id === place_id
      );
      // console.log(selected)
      setDestination(selected ?? {});
      // console.log(destination)
    }

    function updateLastPlace() {
      setTraversed(old => {
          if (old.length === 0) return old
          
      
          const lastIndex = old.length - 1
          const secondLastIndex = old.length - 2
      
          return old.map((place, index) => {
            if (index === secondLastIndex) {
              return { ...place, visited: false, last_place: false}
            }
      
            if (index === lastIndex) {
              return { ...place, last_place: true }
            }
            else {
              return { ...place, last_place: false }
            }
      
            // return place
          })
        })
      }

    const clickHandlerBegin = async()=>{
      const info = await get_shotest_path_from_des_to_target_api(departure.place_id, destination.place_id)
      const path = info.path
      const distance = info.distance
      // console.log(info)

      const placeById = new Map(
        places.map(place => [place.place_id, place])
      );
      // console.log(placeById)

      const orderedPlaces = path
        .map(id => placeById.get(id))
        .filter(Boolean); // remove missing ones safely
        // console.log(orderedPlaces)

      const first_place = orderedPlaces[0]
      const second_place = orderedPlaces[1]

      const distance_twn_place = await get_distance_between_neighbors_by_id(first_place.place_id, second_place.place_id)
      setDistance(distance_twn_place)
      const initial_steps = [first_place, {...second_place, distance:distance_twn_place}]
      setTraversed(initial_steps)
      updateLastPlace()
      // we create copy of initial place and throw away first two place because they are already displayed in time line
      const makeNextAvailable = structuredClone(orderedPlaces)
      // hrow away first two place
      makeNextAvailable.shift()
      makeNextAvailable.shift()

      setRoadMap(makeNextAvailable)
      // console.log(makeNextAvailable)
      

    }
    




    return (
      <Group grow align="flex-start">
        
        {/* LEFT SIDE */}
        <Stack gap="xs">
          <Select
            label="Start"
            placeholder="Pick/Insert value"
            data={selectData}
            onChange={depature_select_handler}
            searchable
          />
  
          <Text ta="center">Or</Text>
  
          <Button color="indigo">Scan QR 1</Button>
        </Stack>
  
        {/* RIGHT SIDE */}
        <Stack gap="xs">
            <Select
            label="Destination"
            placeholder="Pick/Insert value"
            data={selectData}
            onChange={destination_select_handler}
            searchable
            />
            <Text ta="center">Or</Text>
            <Link to="/timeline">
              <Button color="teal" onClick={clickHandlerBegin}>Begin</Button>
            </Link>
        </Stack>
  
      </Group>
    )
  }
  

export default Init