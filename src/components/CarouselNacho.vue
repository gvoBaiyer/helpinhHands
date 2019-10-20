<template>
 <v-card height="10px">
    <v-carousel
      :continuous="true"
      :cycle="true"
      :show-arrows="false"
      hide-delimiter-background
      delimiter-icon="mdi-minus"
    >
      <v-carousel-item
        v-for="(slide, i) in getSlides"
        :key="i"
      >
        <v-sheet
          color="grey"
          tile
        >
          <v-row
            class="fill-height"
            align="center"
            justify="center"
          >
            <div class="display-6">{{ slide }}</div>
          </v-row>
        </v-sheet>
      </v-carousel-item>
    </v-carousel>
  </v-card>
</template>

<script>
  import { mapGetters } from 'vuex';
  export default {
    data () {
      return {

      }
    },
    computed: {
      ...mapGetters([
        'getSlides',
      ]),
    },
  }
</script>