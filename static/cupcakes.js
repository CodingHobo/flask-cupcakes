"use strict";

/** The static JS file to be used with index.html to dynamically create, modify, or delete cupcakes */
const IMG_DIMENSION = "100px";

const $cupcakeAddForm = $("#cupcake-add-form");
const $flavor = $("#flavor");
const $size = $("#size");
const $rating = $("#rating");
const $image_url = $("#image_url");

const $cupcakesList = $("#cupcakes-list");

showCupcakesList();

/**Async function that gets the list of cupcakes from the API
 * Displays the list of cupcakes in the dom
 */
async function showCupcakesList() {
  const response = await axios({
    method: "GET",
    url: "/api/cupcakes",
  });
  console.log(response);
  const cupcakes = response.data.cupcakes;

  for (let cupcake of cupcakes) {
    displayCupcake(cupcake);
  }
}

/**Takes a cupcake object and appends it to the dom cupcake list
 * @param {Object} cupcake
 */
function displayCupcake(cupcake) {
  const $cupcake = $("<li>").html(`
      <img src=${cupcake.image_url} height=${IMG_DIMENSION} width=${IMG_DIMENSION}>
      <p>Flavor: ${cupcake.flavor}, Size: ${cupcake.size}, Rating: ${cupcake.rating}</p>
  `);

  $cupcakesList.append($cupcake);
}

/** Handles submission of new cupcake, appends and displays it on the cupcakes list, */
async function handleFormSubmit(evt) {
  evt.preventDefault();

  const resp = await axios({
    method: "POST",
    url: "/api/cupcakes",
    data: {
      flavor: $flavor.val(),
      size: $size.val(),
      rating: $rating.val(),
      image_url: $image_url.val(),
    },
  });
  displayCupcake(resp.data.cupcake);
}

$cupcakeAddForm.on("submit", handleFormSubmit);
