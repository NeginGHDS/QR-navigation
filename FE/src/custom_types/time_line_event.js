function Place(id, place_id, name, description, floor, section, visited=false, last_place=false, llm_output=false, distance=0) {
    this.id = id
    this.place_id = place_id
    this.name = name
    this.description = description
    this.floor = floor
    this.section = section
    this.visited = visited
    this.last_place = last_place
    this.llm_output = llm_output
    this.distance = distance
  }

export default Place