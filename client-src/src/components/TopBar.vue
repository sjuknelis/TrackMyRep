<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">
        <img src="icon-wide.png" />
        <span>TrackMyRep</span>
      </a>
    </div>
  </nav>
</template>

<script setup></script>

<style scoped>
.container-fluid {
  justify-content: center;
}
.navbar-brand {
  color: white;
}
.navbar {
  background-color: hsl(197deg 65.3% 48.2%) !important;
}
img {
  height: 2rem;
}
span {
  position: relative;
  bottom: -2px;
  padding-left: .5rem;
}
</style>