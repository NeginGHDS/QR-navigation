import { Timeline, Text, Stack, Paper, Group, Button } from '@mantine/core';
import { IconMapPin, IconLocationPin, IconWalk } from '@tabler/icons-react';
import { SingleEvent } from './single_event';
import classes from "../../custom_css/InfoGrid.module.css"

export function CustomTimeLine({
    readerRef,
    currentPlace, listPlacesInShortestPath, shortPath, 
    setCurrentPlace, setShortPath,  
    traversed, setTraversed, places, destination, 
    reachedToDestination, setReachedToDestination, 
    roadMap, setRoadMap,
    availablePlaceForCurrentPlace, setAvailablePlaceForCurrentPlace,
    distance, setDistance, departure
 }){
    
    // console.log("traversed so far:", traversed)
    const active_lines = traversed.length > 1 ? traversed.length - 1 : 0;
    // console.log(active_lines)
    return(
        <Stack className={classes.paper} >
            <Information departure={departure} destination={destination} distance={distance}/>
            <Paper shadow="lg" withBorder p="xl" radius="md">
                <Timeline mt={10} active={active_lines} color="red" bulletSize={32} lineWidth={6}>
                    {traversed.map((plc, index) => (<SingleEvent readerRef={readerRef} departure={departure} currentPlace={currentPlace} listPlacesInShortestPath={listPlacesInShortestPath} shortPath={shortPath} 
                    setCurrentPlace={setCurrentPlace} setShortPath={setShortPath} the_place={plc} setTraversed={setTraversed} traversed={traversed} 
                    places={places} destination={destination}
                    reachedToDestination={reachedToDestination} setReachedToDestination={setReachedToDestination} 
                    roadMap={roadMap} setRoadMap={setRoadMap} key={index}
                    availablePlaceForCurrentPlace={availablePlaceForCurrentPlace} setAvailablePlaceForCurrentPlace={setAvailablePlaceForCurrentPlace}
                    index={index} activeIndex={active_lines}
                    distance={distance} setDistance={setDistance}/>))}
                </Timeline>
            </Paper>
        </Stack>
    )
}


function Information({departure, destination, distance}){
    // console.log(departure)
    return(
        <Group>
            <Paper shadow="xs" withBorder p="md" radius="md" key={departure.id}>
                <Group justify="space-between">
                <Text size="xs" className={classes.title}>
                    Start
                </Text>
                <IconLocationPin className={classes.icon} size={25} stroke={1.1} />
                </Group>

                <Group align="flex-end" gap="xs" mt={25}>
                <Text className={classes.value}>{departure.name}</Text>
                </Group>
            </Paper>

            <Paper shadow="xs" withBorder p="md" radius="md" key={destination.id}>
                <Group justify="space-between">
                <Text size="xs"  className={classes.title}>
                    Finish
                </Text>
                <IconMapPin className={classes.icon} size={25} stroke={1.1} />
                </Group>

                <Group align="flex-end" gap="xs" mt={25}>
                <Text className={classes.value}>{destination.name}</Text>
                </Group>
            </Paper> 
            <Paper shadow="xs" withBorder p="md" radius="md" key="all distances">
                <Group justify="space-between">
                <Text size="xs"  className={classes.title}>
                    Distance
                </Text>
                <IconWalk className={classes.icon} size={25} stroke={1.1} />
                </Group>

                <Group align="flex-end" gap="xs" mt={25}>
                <Text className={classes.value}>{distance} meters</Text>
                </Group>
            </Paper>      
        </Group>
    )
}