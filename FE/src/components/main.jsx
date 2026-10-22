import {CustomTimeLine} from './time_line/time_line'
import Place from '../custom_types/time_line_event'
import { useState, useEffect } from 'react'
import Init from './start_end/specify_start_end'
import { get_all_places_api } from '../APIs/place'
import { VeryFirstPage } from './first_page'
import { Routes, Route } from "react-router-dom";
import { BrowserRouter } from "react-router-dom";
import { useRef } from "react";


function Main(){

    // const p = [new Place(0, "WC", "here you can pee", 0, "Art", true), new Place(1, "WC1", "here you can pee1", 0, "Art", true), new Place(2, "WC1", "here you can pee1", 0, "Art", false, true)]
    const [places, setPlaces] = useState([])
    const [departure, setDeparture] = useState({})
    const [destination, setDestination] = useState({})
    const [roadMap, setRoadMap] = useState([])
    const [traversed, setTraversed] = useState([])
    const [reachedToDestination, setReachedToDestination] = useState(false)
    const [availablePlaceForCurrentPlace, setAvailablePlaceForCurrentPlace] = useState([])
    const [distance, setDistance] = useState(0)
    const [shortPath, setShortPath] = useState({})
    const [listPlacesInShortestPath, setListPlacesInShortestPath] = useState([])
    const [currentPlace, setCurrentPlace] = useState({})
    const readerRef = useRef(null);

    // console.log("departure", departure)


    

    useEffect(() => {
      if (shortPath?.path) {
        const all_places_in_shortest_path = places.filter(item =>
          shortPath.path.includes(item.place_id)
        )

        console.log(traversed)
    
        setListPlacesInShortestPath(all_places_in_shortest_path)
      }
    }, [shortPath])

    
    useEffect(() => {
        const fetchPlaces = async () => {
            const all_places = await get_all_places_api();
            
            const mappedPlaces = all_places.map(p =>
                new Place(
                  p.id,
                  p.place_id,
                  p.name,
                  p.description,
                  p.floor,
                  p.section,
                  p.visited ?? false,
                  p.last_place ?? false,
                )
              );
            
            setPlaces(mappedPlaces);
          };
        
          fetchPlaces();
      }, []);
    // console.log(roadMap)
    return(
      <BrowserRouter>
        <Routes>
        <Route path="/" element={<VeryFirstPage readerRef={readerRef} setCurrentPlace={setCurrentPlace} setShortPath={setShortPath} traversed={traversed} setRoadMap={setRoadMap} setTraversed={setTraversed} places={places} departure={departure} setDeparture={setDeparture} destination={destination} setDestination={setDestination} setDistance={setDistance}/>} />
        <Route path="*" element={<Init traversed={traversed} setRoadMap={setRoadMap} setTraversed={setTraversed} places={places} departure={departure} setDeparture={setDeparture} destination={destination} setDestination={setDestination} setDistance={setDistance}/>}/>
        <Route path="/timeline" element={<CustomTimeLine readerRef={readerRef} currentPlace={currentPlace} listPlacesInShortestPath={listPlacesInShortestPath} shortPath={shortPath} setCurrentPlace={setCurrentPlace} setShortPath={setShortPath} traversed={traversed} setTraversed={setTraversed} 
              places={places} destination={destination} reachedToDestination={reachedToDestination} 
              setReachedToDestination={setReachedToDestination} roadMap={roadMap} setRoadMap={setRoadMap}
              availablePlaceForCurrentPlace={availablePlaceForCurrentPlace} setAvailablePlaceForCurrentPlace={setAvailablePlaceForCurrentPlace}
              distance={distance} setDistance={setDistance} departure={departure}
              />} />
      </Routes>
    </BrowserRouter>
    )
}

export default Main