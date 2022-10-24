<template>
  <div v-if="data" class="card">
    <p class="title">{{ data.bill.short_title }}</p>
    <i>{{ data.question }} – {{ data.bill.title }}</i>
    <div class="row">
      <div class="col-6">
        <p v-if="repInfo">{{ repInfo.bio.first_name }} {{ repInfo.bio.last_name }} ({{ repInfo.bio.party.charAt(0) }}-{{ stateAbbr }}-{{ districtNumber }}) voted <b>{{ data.vote.person }}</b> on this bill.</p>
      </div>
      <div class="col-6">
        <b>Breakdown by Party</b>
        <table>
          <tr>
            <th></th>
            <th>Yes</th>
            <th>No</th>
            <th>P/NV</th>
          </tr>
          <tr v-for="party in PARTIES" :key="party">
            <td>{{ capitalize(party) }}</td>
            <td :style="`background-color: rgba(${PARTY_COLORS[party]},${.5 * data.vote.parties[party].yes / getPartyTotal(data.vote.parties[party])})`">
              {{ data.vote.parties[party].yes }}
            </td>
            <td :style="`background-color: rgba(${PARTY_COLORS[party]},${.5 * data.vote.parties[party].no / getPartyTotal(data.vote.parties[party])})`">
              {{ data.vote.parties[party].no }}
            </td>
            <td :style="`background-color: rgba(${PARTY_COLORS[party]},${(.5 * data.vote.parties[party].present + data.vote.parties[party].not_voting) / getPartyTotal(data.vote.parties[party])})`">
              {{ data.vote.parties[party].present + data.vote.parties[party].not_voting }}
            </td>
          </tr>
          <tr v-if="totals">
            <td>Total</td>
            <td>{{ totals.yes }}</td>
            <td>{{ totals.no }}</td>
            <td>{{ totals.not_voting }}</td>
          </tr>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps,computed } from 'vue';

const props = defineProps(["data","repData"]);
const PARTIES = ["democratic","republican","independent"];
const PARTY_COLORS = {
  "democratic": "12,71,195",
  "republican": "212,52,45",
  "independent": "128,128,128"
};
const capitalize = s => s.charAt(0).toUpperCase() + s.slice(1);

function getTotals(partyData) {
  const result = {
    yes: 0,
    no: 0,
    not_voting: 0
  };
  for ( const party of PARTIES ) {
    result.yes += partyData[party].yes;
    result.no += partyData[party].no;
    result.not_voting += partyData[party].present + partyData[party].not_voting;
  }
  return result;
}
const totals = computed(() => props.data ? getTotals(props.data.vote.parties) : null);

function getPartyTotal(partyVote) {
  return partyVote.yes + partyVote.no + partyVote.present + partyVote.not_voting; 
}

const stateAbbr = computed(() => props.repData ? props.repData.results[0].address_components.state : null);
const districtNumber = computed(() => props.repData ? props.repData.results[0].fields.congressional_districts[0].name.split(" ")[2] : null);
const repInfo = computed(() => props.repData ? props.repData.results[0].fields.congressional_districts[0].current_legislators[0] : null);
</script>

<style scoped>
.card {
  margin-bottom: 1rem;
  padding: 1rem;
}
.title {
  font-size: 1.2rem;
  margin-top: 0;
  margin-bottom: 0;
}
.col-6 {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.col-6 * {
  text-align: center;
}
table,tr,td,th {
  border-collapse: collapse;
}
td:first-child {
  font-weight: bold;
}
td,th {
  width: 25%;
  text-align: center;
}
.table-row-democratic {
  background-color: rgba(12,71,195,.5);
}
.table-row-republican {
  background-color: rgba(212,52,45,.5);
}
</style>
