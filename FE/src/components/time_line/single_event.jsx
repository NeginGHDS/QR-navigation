
import { Timeline, Text, Button, Group, Stack, Select, Loader } from '@mantine/core';
import { IconWalk, IconCheck, IconMapPin} from '@tabler/icons-react'; 
import { useEffect, useState } from 'react'
import { get_neighbors_by_id, get_shotest_path_from_des_to_target_api, get_distance_between_neighbors_by_id } from '../../APIs/neighbor';
import { Link } from 'react-router-dom';
import {Html5QrcodeScanner} from "html5-qrcode";
import { interact_with_agent } from '../../APIs/agent';

export function SingleEvent({
  readerRef,
  departure, currentPlace, listPlacesInShortestPath, shortPath,
  setCurrentPlace, setShortPath, the_place, 
  setTraversed, traversed, 
  places, destination, 
  reachedToDestination, setReachedToDestination, 
  roadMap, setRoadMap,
  availablePlaceForCurrentPlace, setAvailablePlaceForCurrentPlace,
  index, activeIndex,
  distance, setDistance
}){
    const walk_icon = <IconWalk size={42} />
    const check_icon = <IconCheck size={42} />
    const map_pin_icon = <IconMapPin size={42} />
    const line_type = the_place?.visited ? "solid" : "dashed"
  //   const line_type =
  // index > activeIndex ? "solid" : "dashed";
    

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
              return { ...place, last_place: false, visited: true }
            }
      
            // return place
          })
        })
      }
    
      let icon = check_icon
      if (!the_place.visited && !the_place.last_place){
        icon = walk_icon
      }
      if (!the_place.visited && the_place.last_place){
        icon = map_pin_icon
      }
      if (the_place.visited ){
        icon = check_icon
      }

    // console.log(the_place)


    const mapPlacesToSelectData_for_available_data = (all_neighbors) => {
      const groups = {};
    
      all_neighbors.forEach(place => {
        const section = place.section || "Other";
    
        if (!groups[section]) {
          groups[section] = [];
        }
        
        // if(!traversed.some(a_traversed_place=>a_traversed_place.place_id == place.place_id) ){
          groups[section].push({
            value: String(place.place_id), // Select value
            label: place.name,        // Display text
          });
        // }

      });
    
      return Object.entries(groups).map(([group, items]) => ({
        group,
        items,
      }));
    };


    // const availablePlaces = mapPlacesToSelectData_for_available_data()
    // let availablePlaces = []

    // const goToNextStepHandler = async()=> {
      
    //   const lastelemet = traversed.at(-1);
    //   if (lastelemet.place_id == destination.place_id){
    //     // console.log("you reached to Dest.")
    //     setReachedToDestination(true)
    //   }
    //   else{
    //     const last_place = traversed.at(-1)
    //     const next_place = roadMap.at(0)
    //     const distance_between_places = await get_distance_between_neighbors_by_id(last_place.place_id, next_place.place_id)
    //     setDistance(old_dis=>{
    //       return old_dis + distance_between_places
    //     })
    //     // removes the first element
    //     setRoadMap(old => old.slice(1));
    //     setTraversed(old => [...old, {...next_place, distance:distance_between_places}]);
    //     updateLastPlace()
        
    //     // console.log("pass")
    //   }
      
    // }

    const goToNextStepByDropDownHandler = async(next_place_id) => {
      console.log("next_place_id", next_place_id)
      // next_place is the id of next place not object of next place
      // console.log("input of goToNextStepByDropDownHandler is:", next_place_id)
      const distance_between_places = await get_distance_between_neighbors_by_id(traversed.at(-1).place_id, next_place_id)
      setDistance(old_dis=>{
        return old_dis + distance_between_places
      })
      
      const shortest_path = await get_shotest_path_from_des_to_target_api(next_place_id, destination.place_id) // {"path":["id_2", "id_3", "id_4"],  "distance":6}
      setShortPath(shortest_path)
      // console.log("new path from", next_place_id, "to", destination.place_id, "is", shortest_path)
      const path = shortest_path.path

      const placeById = new Map(
        places.map(place => [place.place_id, place])
      );
      // console.log(placeById)

      const orderedPlaces = path
        .map(id => placeById.get(id))
        .filter(Boolean); // remove missing ones safely
        // console.log("orderedPlaces in drop down handler:", orderedPlaces)
        const very_next_step = {...orderedPlaces.shift(), distance:distance_between_places}
        setTraversed(old_state=>{
          return [...old_state, very_next_step]
        })

        setCurrentPlace(very_next_step)

        updateLastPlace()
        // we update the raodmap based on current selection!
        setRoadMap(orderedPlaces)

        // console.log("orderedPlaces in drop down handler after shift:", orderedPlaces)      
    }



    const call_llm = async() => {
      let response;
      if (index === activeIndex-1){
        // if we do not use if, for each elemet in timeline llm will be called.
        // console.log("calling llm index is:", index)
        response = await interact_with_agent(destination, departure, shortPath, traversed, listPlacesInShortestPath, currentPlace)
      }
      // console.log("agent_response", response)
      setTraversed(oldState => {
        if (oldState.length < 2) return oldState;
      
        const index = oldState.length - 2;
      
        return oldState.map((item, i) => {
          if (i === index) {
            return {
              ...item,
              llm_output: response
            };
          }
          return item;
        });
      });
    };

    // const call_llm = async() => {
    //   const response = await interact_with_agent(destination, departure, shortPath, traversed, listPlacesInShortestPath, currentPlace)
    //   // console.log("agent_response", response)
    //   setTraversed(oldState => {
    //     if (oldState.length < 2) return oldState;
    
    //     const newState = [...oldState];
    //     const oneToLastIndex = newState.length - 2;
    //     const one_to_last_place = newState[oneToLastIndex];
    
    //     // newState[oneToLastIndex] = {
    //     //   ...one_to_last_place,
    //     //   llm_output: "I'm updated version!" + Math.random()
    //     // };

    //     newState[oneToLastIndex] = {
    //       ...one_to_last_place,
    //       llm_output: response
    //     };
    
    //     return newState;
    //   });
    // };
    
    
    // we use useEffect and put dependency on "traversed" to update the content when "traversed" is changed/modified.
    useEffect(() => {
      const lastelemet = traversed.at(-1);
      if (lastelemet.place_id == destination.place_id){
        console.log("ypu reached to Dest.")
        setReachedToDestination(true)
      }

      const get_neighbors_for_given_place = async () => {
        const all_paths_to_traget_in_given_place = await get_neighbors_by_id(the_place.place_id, destination.place_id); // [['id_0', 'id_2', 'id_3', 'id_4'], ['id_2', 'id_3', 'id_4'], ['id_4']]
        // console.log("all_paths_to_traget_in_given_place", all_paths_to_traget_in_given_place)
        // first we need to create list of ids of nodes that are traveresed so far:
        const list_of_ids_of_traversed_places = traversed.map(given_place=>given_place.place_id) // ["id_0", "id_2"]
        // console.log("list_of_ids_of_traversed_places", list_of_ids_of_traversed_places)
        // then we need to remove those paths that has place(place_id) that is already traversed, we need to conver list to set in order to be able to call .has function because list does not has such function.
        const traversedSet = new Set(list_of_ids_of_traversed_places);
        const list_of_all_paths_leads_to_target_without_visiting_place_twice = all_paths_to_traget_in_given_place.filter(list =>
          list.every(x => !traversedSet.has(x))
        );
        // console.log("all paths lead sto target", reslist_of_all_paths_leads_to_target_without_visiting_place_twiceult)
        // since in every place we should show just next place, we took the first elements in the filtered list.
        const next_places = list_of_all_paths_leads_to_target_without_visiting_place_twice.map(a_list => a_list[0]); // ["id_2","id_4"]
        // console.log("next_places", next_places)
        // since we need more information to be displayed in drop down, we should map this list of ids to actual places
        
        const set_of_next_places = new Set(next_places);
        const more_detailed_info_for_given_ids = places.filter(obj => set_of_next_places.has(obj.place_id));
        // console.log("more info", result)




        const availablePlaces = mapPlacesToSelectData_for_available_data(more_detailed_info_for_given_ids)
        setAvailablePlaceForCurrentPlace(availablePlaces)

        // console.log("all neighbors", all_neighbors)
        // console.log("available Places", availablePlaces)
        // console.log("traversed", traversed)
        await call_llm()
        

      };
    
      get_neighbors_for_given_place();
      
      
      

    }, [roadMap]);

    return(
    <Timeline.Item bullet={ icon } lineVariant={line_type} title={the_place.name} key={the_place.place_id}>
        <Group justify="space-between" align="center" w="100%">
            
            {/* LEFT: texts stacked vertically */}
            <Stack gap={0}>
                {/* <Text c="dimmed" size="sm">
                    {the_place.description}
                </Text> */}
                <Group>
                  { index ?
                    <Text size="xs" c="gray">
                        Distance between places: {the_place.distance} meters
                    </Text>
                    : <></>
                  }
                 { index==activeIndex ?
                  <Text size="xs" c="gray">
                  Walked so far: {distance} meters
                  </Text>
                    : <></>
                  }
                </Group>
                

                  { index === activeIndex ? <></> : index < activeIndex && the_place.llm_output && the_place.last_place !== 1 ? <Text fw={200} style={{ whiteSpace: "pre-wrap" }}> {the_place.llm_output}</Text> : <Loader/>}
                  
                

            {/* RIGHT: button */}
            {!the_place.visited && the_place.last_place && !reachedToDestination ? 
            <SingleEventAction  key={the_place.id} readerRef={readerRef} setCurrentPlace={setCurrentPlace} updateLastPlace={updateLastPlace} traversed={traversed} destination={destination} roadMap={roadMap} availablePlaceForCurrentPlace={availablePlaceForCurrentPlace} goToNextStepByDropDownHandler={goToNextStepByDropDownHandler} setReachedToDestinatio={setReachedToDestination} setDistance={setDistance} setRoadMap={setRoadMap} setTraversed={setTraversed} />            
            : <></>}

            {the_place.last_place && reachedToDestination ? <BackToFirstPage /> : <></>}

          </Stack>

        </Group>
    </Timeline.Item>
    )
}

function SingleEventAction({ readerRef, setCurrentPlace, updateLastPlace, traversed, destination, roadMap, availablePlaceForCurrentPlace, goToNextStepByDropDownHandler, setReachedToDestination, setDistance, setRoadMap, setTraversed}){

  const goToNextStepHandler = async()=> {
      
    const lastelemet = traversed.at(-1);
    if (lastelemet.place_id == destination.place_id){
      // console.log("you reached to Dest.")
      setReachedToDestination(true)
    }
    else{
      const last_place = traversed.at(-1)
      const next_place = roadMap.at(0)
      setCurrentPlace(next_place)
      
      const distance_between_places = await get_distance_between_neighbors_by_id(last_place.place_id, next_place.place_id)
      setDistance(old_dis=>{
        return old_dis + distance_between_places
      })
      // removes the first element
      setRoadMap(old => old.slice(1));
      setTraversed(old => [...old, {...next_place, distance:distance_between_places}]);
      updateLastPlace()
      
      // console.log("pass")
    }
    
  }

  const scan_qr_handler_tl = () => {
    const scanner = new Html5QrcodeScanner("reader_tl", {
      fps: 10,
      qrbox: 250,
    });
  
    readerRef.current = scanner;
  
    scanner.render(async (decodedText) => {
      console.log("Scanned in TL:", decodedText);
  
      const the_place = JSON.parse(decodedText);
  
      await goToNextStepByDropDownHandler(the_place.place_id);
  
      scanner.clear().then(() => {
        readerRef.current = null;
      });
    });
  };



  return(
    <Group grow align="center" >
      <Stack gap="xs">
        <Select
          justify="center"
          placeholder="Pick/Insert Next Place(List of neighbors that have path to destination)"
          data={availablePlaceForCurrentPlace}
          onChange={goToNextStepByDropDownHandler}
          searchable
        />
        <Text ta="center">Or</Text>
        <Button onClick={scan_qr_handler_tl} color="indigo">Scan QR 2</Button>
        <div ref={readerRef} id="reader_tl" style={{ width: "150px" }} />
        <Text ta="center">Or</Text>
        <Button onClick={goToNextStepHandler}>Next Step Based on Shortest Path</Button>
      </Stack>
      
    </Group>
  )
}


function BackToFirstPage({destination}){
  return(
    <Link to="/">
      <Button>Start again</Button>
    </Link>
  )
}