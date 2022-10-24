<template>
  <TopBar />
  <div v-if="data" class="main-container">
    <h5>Relevant vote in Congress:</h5>
    <BillBox :data="data[0]" :repData="repData" />
    <button class="btn btn-outline-primary full-button" @click="popout">See more votes</button>
  </div>
  <div v-else class="main-container">
    <p class="loading-text">Loading...</p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import BillBox from './components/BillBox.vue';
import TopBar from './components/TopBar.vue';
import { getRepData } from './repData';

const data = ref(null);
const repData = ref(null);
(async () => {
  repData.value = await getRepData();
})();

function popout() {
  // eslint-disable-next-line
  chrome.tabs.create({url: `popout/index.html?${encodeURIComponent(JSON.stringify(data.value))}`},() => {});
}

// eslint-disable-next-line
chrome.tabs.query({active: true,currentWindow: true},function(tabs) {
  const interval = setInterval(() => {
    // eslint-disable-next-line
    chrome.tabs.sendMessage(tabs[0].id,{type: "getData"},function(retrieved) {
      if ( retrieved ) {
        data.value = retrieved;
        clearInterval(interval);
      }
    });
  },100);
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
.loading-text {
  text-align: center;
  margin-top: 1rem;
  margin-bottom: 1rem;
}
</style>
