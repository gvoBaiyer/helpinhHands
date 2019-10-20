<template>
  <v-container>
    <v-layout
      text-center
      wrap
    >
      <v-flex xs12>
        <CarouselNacho></CarouselNacho>
      </v-flex>
      <v-flex xs12>
        <v-spacer></v-spacer>
        <v-text-field disabled></v-text-field>
      </v-flex>
      <v-flex xs4>
        <Sidebar></Sidebar>
      </v-flex>
      <v-flex xs8>
        <MapPlaceHolder></MapPlaceHolder>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import Sidebar from './Sidebar.vue';
import MapPlaceHolder from './MapPlaceHolder'
import CarouselNacho from './CarouselNacho'
export default {
  components: {
    Sidebar,
    MapPlaceHolder,
    CarouselNacho
  },
};
</script>
