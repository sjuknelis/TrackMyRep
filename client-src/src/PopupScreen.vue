<template>
  <TopBar />
  <div class="main-container">
    <h5>Relevant vote in Congress:</h5>
    <BillBox :data="data[0]" />
    <button class="btn btn-outline-primary full-button" @click="popout">See more votes</button>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import BillBox from './components/BillBox.vue';
import TopBar from './components/TopBar.vue';

const data = ref([{"bill":{"title":"To prohibit the importation of energy products of the Russian Federation, and for other purposes.","short_title":"ewrjwirweojrworSuspending Energy Imports from Russia Act","vote_uri":"https://api.propublica.org/congress/v1/117/house/sessions/2/votes/70.json","id":70,"stamp":24267},"vote":{"person":"Yes","parties":{"democratic":{"yes":220,"no":2,"present":0,"not_voting":0,"majority_position":"Yes"},"republican":{"yes":194,"no":15,"present":0,"not_voting":2,"majority_position":"Yes"},"independent":{"yes":0,"no":0,"present":0,"not_voting":0}}}}]);

function popout() {
  // eslint-disable-next-line
  chrome.tabs.create({url: `popout/index.html?${encodeURIComponent(JSON.stringify(data.value))}`},() => {});
}

// eslint-disable-next-line
chrome.tabs.query({active: true,currentWindow: true},function(tabs) {
  // eslint-disable-next-line
  chrome.tabs.sendMessage(tabs[0].id,{type: "getData"},function(retrieved) {
    data.value = retrieved;
  });
});
</script>

<style>
html,body {
  width: 600px;
}
body {
  display: flex;
  justify-content: center;
  font-family: "Avenir";
}
#app {
  width: 100vw;
}
.main-container {
  margin-top: 10px;
  padding-left: 10px;
  padding-right: 10px;
}
.full-button {
  width: 100%;
  margin-top: -5px;
  margin-bottom: 10px;
}
</style>
