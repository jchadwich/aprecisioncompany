mapboxgl.accessToken = "pk.eyJ1IjoiYWN1cmxleTMxIiwiYSI6ImNsMDVqYmRzYTFuM2UzaXFnMThuMnE5NHMifQ.DaCM5UwTwkuLo02YUKQpFA"


const renderMeasurementsMap = () => {
  const map = new mapboxgl.Map({
    container: 'measurements-map', // container ID
    style: "mapbox://styles/mapbox/light-v10",
    center: [-74.5, 40], // starting position [lng, lat]
    zoom: 9, // starting zoom
  });
}
