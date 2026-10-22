from fastapi import FastAPI
# here we include routes we have developed in order to include them and put them under umbrella of app
from backend.utils.routes.places_route import place_router
from backend.utils.routes.neighbors_route import neighbors_router
from backend.utils.routes.agents_route import agent_router
# we heed CORS in order to specify which frontend is eligible to contact to backend
from fastapi.middleware.cors import CORSMiddleware


from backend.database.controlers.places import insert_place_controller
from backend.database.controlers.neighbors import insert_neighbor_controller
from backend.database.tabels import create_places_table, create_neighbors_table




app = FastAPI(
    title="Backend API for handling call to db and agent",
    version="1.0.0",
    description="API providing detailed information on places we have and possible routing for given point of user."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5173", "http://localhost:5173"],  # Defines which frontends are allowed to call your API.
    allow_credentials=True, # Enables sending:Cookies, Authorization headers, Session tokens, When you need it: You rely on browser-stored auth, You use session-based auth
    allow_methods=["*"], # Which HTTP methods the browser may use. GET, POST, PUT, PATCH, DELETE
    allow_headers=["*"], # Which request headers frontend JS can send. Authorization, Content-Type
)

app.include_router(place_router)
app.include_router(neighbors_router)
app.include_router(agent_router)

# create_places_table()
# create_neighbors_table()
# insert_place_controller()
# insert_neighbor_controller()



