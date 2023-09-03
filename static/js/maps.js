mapboxgl.accessToken = "pk.eyJ1IjoiYWN1cmxleTMxIiwiYSI6ImNsMDVqYmRzYTFuM2UzaXFnMThuMnE5NHMifQ.DaCM5UwTwkuLo02YUKQpFA"

/*
const renderMeasurementsMap = () => {
  const map = new mapboxgl.Map({
    container: "map",
    container: 'measurements-map', // container ID
    style: "mapbox://styles/mapbox/light-v10",
    center: [-74.5, 40], // starting position [lng, lat]
    zoom: 9, // starting zoom
  });
}
*/

const MAPBOX_CONFIG = {
  style: "mapbox://styles/mapbox/streets-v12",
  center: [-74.5, 40],
  zoom: 12,
}

class MeasurementsMap {
  constructor(containerId, projectId) {
    this.projectId = projectId;
    this.map = new mapboxgl.Map({ ...MAPBOX_CONFIG, container: containerId })
  }
}
