<template>
  <TopBar />
  <div class="row main-container">
    <div v-if="repData" class="col-3 rep-info">
      <img class="rep" :src="getRepImage(repInfo.bio.first_name,repInfo.bio.last_name)" />
      <h3>{{ repInfo.bio.first_name }} {{ repInfo.bio.last_name }}</h3>
      <p>{{ districtName }} of {{ convertState(stateAbbr) }} – {{ PARTY_ADJECTIVES[repInfo.bio.party] }}</p>
      <p>Up for election: {{ electionYear }}</p>
      <p>
        <i class="fa-brands fa-twitter"></i>
        <a :href="`https://twitter.com/${repInfo.social.twitter}`" target="_blank">@{{ repInfo.social.twitter }}</a>
      </p>
      <p>
        <i class="fa-brands fa-youtube"></i>
        <a :href="`https://youtube.com/channel/${repInfo.social.youtube_id}`" target="_blank">Rep. {{ repInfo.bio.last_name }} on YouTube</a>
      </p>
      <p>
        <i class="fa-solid fa-earth-americas"></i>
        <a :href="repInfo.contact.url" target="_blank">{{ repInfo.contact.url.split("https://")[1] }}</a>
      </p>
      <p>
        <i class="fa-solid fa-phone"></i>
        <a :href="`tel:${repInfo.contact.phone}`">{{ repInfo.contact.phone }}</a>
      </p>
    </div>
    <div class="col-9 bill-boxes">
      <h3>Most Relevant Votes</h3>
      <BillBox :data="data[0][0]" :repData="repData" />
      <BillBox :data="data[0][1]" :repData="repData" />
      <BillBox :data="data[0][2]" :repData="repData" />
      <hr />
      <h3>Other Recent Votes</h3>
      <BillBox :data="data[1][0]" :repData="repData" />
      <BillBox :data="data[1][1]" :repData="repData" />
      <BillBox :data="data[1][2]" :repData="repData" />
    </div>
  </div>
</template>

<script setup>
import { ref,computed } from 'vue';
import BillBox from './components/BillBox.vue';
import TopBar from './components/TopBar.vue';
import { getRepData } from './repData';
import { repImages } from './repImages';
import { convertState } from './convertState';

const PARTY_ADJECTIVES = {
  "Democrat": "Democratic Party",
  "Republican": "Republican Party",
  "Independent": "Independent"
};

const data = ref(JSON.parse(decodeURIComponent(location.search.slice(1))));
const repData = ref(null);
(async () => {
  repData.value = await getRepData();
})();

const stateAbbr = computed(() => repData.value ? repData.value.results[0].address_components.state : null);
const districtName = computed(() => repData.value ? repData.value.results[0].fields.congressional_districts[0].name : null);
const repInfo = computed(() => repData.value ? repData.value.results[0].fields.congressional_districts[0].current_legislators[0] : null);
let electionYear = Math.ceil(new Date().getFullYear() / 2) * 2;
if ( new Date().getMonth() == 11 ) electionYear += 2;

// eslint-disable-next-line
function getRepImage(repFirstName,repLastName) {
  const possible = repImages.filter(item => item.indexOf(`${repFirstName}_${repLastName}`) > -1);
  return possible[0];
}
</script>

<style>
body {
  display: flex;
  justify-content: center;
  font-family: "Avenir";
}
#app {
  width: 100vw;
}
.main-container {
  max-width: 90vw;
  margin: auto;
  padding-top: 10px;
}
.rep-info a {
  margin-left: .5em;
}
.rep-info,.bill-boxes {
  height: calc(100vh - 80px);
  overflow-y: scroll;
}
img.rep {
  width: 100%;
  border-radius: 10px;
  padding-bottom: .5rem;
}
</style>
