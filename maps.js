// Create map instance
const map = new maplibregl.Map({
    //This container is to tag this id 'map' in html to render
    container: 'map',

    //Fetch World map vectors and styles
    //style: 'https://maplibre.org', // https://maplibre.org, https://openfreemap.org
    style: {
        "version": 8,
        "source": {},
        "layer": [
            {
                "id": "background",
                "type": "background",
                "paint": { "background-color": "#2f3640" }
            }
        ]
    },
    //Set the starting coordinates on hightway [Longitude, Latitude]
    center: [-84.3896, 33.7410],

    //Set zoom levels
    //zoom: 13,

    //Set camera angle backwards to create the 3D perspective
    //pitch: 0,

    //Rotate camera heading direction (nagative to left)
    //bearing: 0
});