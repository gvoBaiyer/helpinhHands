<template>
    <Map @mapClick="onMapClick"></Map>
</template>

<script>
import Map from './Map.vue';
import { mapGetters } from 'vuex';
export default {
  components: {
    Map
  },
  methods: {
    onMapClick(e) {
      this.$store.commit('setNews', null);
      this.$store.commit('setHazards', null);
      this.$store.commit('setProvince', e.title);
      this.$store.dispatch('setCountry', e.mapId).then(() => {});
      this.$store.dispatch('setNews', e.mapId).then(() => {});
    }
  },
  computed: {
    ...mapGetters([
      'getProvince',
    ]),
  },
}
</script>