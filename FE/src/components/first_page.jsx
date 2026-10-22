import { Container, Image, SimpleGrid, Text, ThemeIcon, Title, Box, Select, Button, Stack, Group, Flex, RingProgress } from '@mantine/core';
// import IMAGES from './images'
import accounttt from './images/accountants.svg'
import qr from './images/qr.png'
import dd from './images/dropdown.png'
import classes from '../custom_css/FeaturesImages.module.css';
import classes2 from '../custom_css/zoom.module.css'
import { Link } from "react-router-dom";
import {Html5QrcodeScanner} from "html5-qrcode";
import { get_shotest_path_from_des_to_target_api, get_distance_between_neighbors_by_id } from '../APIs/neighbor';

const data = [
  { acttion: "qr_scan",
    image: qr,
    title: 'Scan QR Code',
    description: 'This option allows you to find your current location by scaning provided QR code',
  },
  {
    acttion: "btn_click",
    image: dd,
    title: 'Select From list',
    description: 'This is an alternative for cases user wants to search and select from provided list of places',
  },
];

export function VeryFirstPage({readerRef, setCurrentPlace, setShortPath, traversed, setRoadMap, setTraversed, places, departure, setDeparture, destination, setDestination, setDistance }) {
  const items = data.map((item, index) => (
    
      <Box className={classes.item} key={item.acttion}>
        <Stack>
          <Text fw={200} fz="h2" className={classes.itemTitle}> {item.title} </Text>
          <Group justify="center">
            <ThemeIcon variant="light" className={classes.itemIcon} size={120} radius="lg">
              <Box className={classes2.zoomWrap}><Image src={item.image}/></Box>
            </ThemeIcon>
            <Text fw={200} >{item.description}</Text>
            {/* {item.acttion=== "qr_scan" ?<QRCodeSection/> : <DropdownSection places={places} setDeparture={setDeparture}/>} */}
          </Group>
        </Stack>
      </Box>
  ));

  const items_actions = data.map((the_item)=>(
    the_item.acttion=== "qr_scan" ?<QRCodeSection readerRef={readerRef} places={places} setDeparture={setDeparture} key={the_item.title}/> : <DropdownSection key={the_item.title} places={places} setDeparture={setDeparture}/>
  ));
  

  const isEmptyObject = (obj) =>
    obj && Object.keys(obj).length === 0;

  return (
    <Container size={700} className={classes.wrapper}>
      <Title fw={300} className={classes.title} order={2}>
        Welcome to <span className={classes.highlight}>locator</span> application!
      </Title>

      <Container size={660} p={0}>
        <Text fw={250}  className={classes.description}>
          This applicatoin helps you to find your target places for visit in more easy and inforamtive way.
        </Text>
      </Container>
      <Flex align="center" gap="xl">
      <RingProgress
        size={60}
        thickness={5}
        sections={[{ value: 100, color: 'blue' }]}
        label={
          <Text c="blue" fw={400} ta="center" size="xl">
            1
          </Text>
        }
      />
        <SimpleGrid cols={{ base: 1, xs: 2 }} spacing={50} mt={30}>
          {items}
          {items_actions}
        </SimpleGrid>
      </Flex>
      <Box mt={20} >
        {!isEmptyObject(departure)? <DestinationSection places={places} setDestination={setDestination}/> : <></>}
      </Box>
      <Box mt={20} >
        {!isEmptyObject(destination)? <StartSection setCurrentPlace={setCurrentPlace} setShortPath={setShortPath} places={places} departure={departure} destination={destination} setDistance={setDistance} setTraversed={setTraversed} setRoadMap={setRoadMap} /> : <></>}
      </Box>
    </Container>
  );
}

function QRCodeSection({readerRef, places, setDeparture}){

  const depature_select_handler = (place_id)=>{
    const selected = places.find(
      place => place.place_id === place_id
    );
    console.log(place_id)
    setDeparture(selected ?? {});
    console.log(selected)
  }
  
  const scan_qr_handler = () => {
    const scanner = new Html5QrcodeScanner("reader", {
      fps: 10,
      qrbox: 250,
    });

    readerRef.current = scanner;

    scanner.render((decodedText) => {
      // console.log("Scanned:", typeof decodedText);
      const the_place = JSON.parse(decodedText);
      depature_select_handler(the_place.place_id)

      // ✅ STOP scanning immediately
      scanner.clear().then(() => {
        // console.log("Scanner stopped");
      });
    });
  };

  return(
    <>
      <Button onClick={scan_qr_handler}>Scan QR Code</Button>
      <div ref={readerRef} id="reader" style={{ width: "150px" }} />
    </>
  )

}

function DropdownSection({places, setDeparture}){

  const mapPlacesToSelectData = () => {
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

  const depature_select_handler = (place_id)=>{
    const selected = places.find(
      place => place.place_id === place_id
    );
    // console.log(place_id)
    setDeparture(selected ?? {});
    // console.log(selected)
  }

  return(
    <Select
            placeholder="Pick/Insert value"
            data={mapPlacesToSelectData()}
            onChange={depature_select_handler}
            searchable
          />
  )
}

function DestinationSection({places, setDestination}){

  const mapPlacesToSelectData = () => {
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


  const destination_select_handler = (place_id)=>{
    const selected = places.find(
      place => place.place_id === place_id
    );
    // console.log(selected)
    setDestination(selected ?? {});
    // console.log(destination)
  }
  return(
    <Flex align="center" gap="xl">
            <RingProgress
        size={60}
        thickness={5}
        sections={[{ value: 100, color: 'blue' }]}
        label={
          <Text c="blue" fw={400} ta="center" size="xl">
            2
          </Text>
        }
      />
      <Select
              w="100%"
              placeholder="Pick/Insert you destination"
              data={mapPlacesToSelectData()}
              onChange={destination_select_handler}
              searchable
            />
    </Flex>
  )

}


function StartSection({ setCurrentPlace, setShortPath, places, departure, destination, setDistance, setTraversed, setRoadMap}){

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
    setShortPath(info)
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
    setCurrentPlace(first_place)
    // console.log(makeNextAvailable)
    
  }
  return(
    <Flex align="center" gap="xl" w="100%">
      <RingProgress
        size={60}
        thickness={5}
        sections={[{ value: 100, color: 'teal' }]}
        label={
          <Text c="teal" fw={400} ta="center" size="xl">
            3
          </Text>
        }
      />
      <Box flex={1}>
      <Link to="/timeline" >
        <Button w="100%" color="teal" onClick={clickHandlerBegin}>Let's explore the area!</Button>
      </Link>
      </Box>
    </Flex>
  )
}