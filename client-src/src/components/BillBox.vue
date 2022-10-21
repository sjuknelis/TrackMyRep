<template>
  <div class="card">
    <p class="title">{{ data.bill.short_title }}</p>
    <i>{{ data.bill.title }}</i>
    <div class="row">
      <div class="col-6">
        <p>Katherine Clark (D-MA-5) voted <b>{{ data.vote.person }}</b> on this bill.</p>
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
          <tr v-for="party in PARTIES" :key="party" :class="`table-row-${party}`">
            <td>{{ capitalize(party) }}</td>
            <td>{{ data.vote.parties[party].yes }}</td>
            <td>{{ data.vote.parties[party].no }}</td>
            <td>{{ data.vote.parties[party].present + data.vote.parties[party].not_voting }}</td>
          </tr>
          <tr>
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
import { defineProps } from 'vue';

const props = defineProps(["data"]);
const PARTIES = ["democratic","republican","independent"];
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

const totals = getTotals(props.data.vote.parties);
</script>

<style scoped>
.card {
  margin-bottom: 1rem;
}
.title {
  font-size: 1.2rem;
  margin-top: 0;
  margin-bottom: 0;
}
.col-6 {
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
