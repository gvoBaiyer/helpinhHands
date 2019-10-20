<template>
            <v-card>
              <v-toolbar>
                    <v-toolbar-items>
                      <v-btn text @click="toggleHistorico()" :disabled='true'>Past</v-btn>
                        <v-btn text @click="toggleActual()" :disabled='true'>Now</v-btn>
                        <v-btn text @click="toggleFuturo()" :disabled='true'>Prediction</v-btn>
                    </v-toolbar-items>
                </v-toolbar>
                <v-flex v-if="isHistorico">
                  <v-card-title> 
                      What's happened
                  </v-card-title>
                </v-flex>
                <v-flex v-if="isActual">
                  <v-card-title> 
                    We need your help!
                  </v-card-title>
                  <v-flex v-if="getProvince == null">
                  <v-card @click='open("https://japantoday.com/category/national/typhoon-hit-areas-brace-for-more-floods-as-heavy-rain-may-douse-again")'>
                  <h4>Typhoon-hit areas brace for more floods</h4>
                  <p>Source: Japan Today</p>
                  </v-card>                    
                  <v-card @click='open("https://www.wfp.org/countries/democratic-republic-congo")'>
                  <h4>World</h4>
                  <p>Source: Word Food Program</p>
                  </v-card>
                  <v-list>
                  </v-list>             
                  </v-flex>
                  <v-card v-if="getHazards!=null">
                  <h4>{{ getHazards[0].title }}</h4>
                  <p>Source: PredictHQ API</p>
                  </v-card>
                  <v-flex v-if="getProvince == 'Dem. Rep. Congo'">                 
                  <v-list>
                    <v-card-title>How can I help?</v-card-title>
                    <v-list-item @click='open("https://www.manosunidas.org")'>Manos unidas</v-list-item>
                    <v-list-item @click='open("https://www.msf.es/")'>Medicos sin fronteras</v-list-item>
                  </v-list>
                  </v-flex>
                  <v-flex v-if="getProvince == 'Brazil'">
                  <v-list>
                    <v-card-title>How can I help?</v-card-title>
                    <v-list-item @click='open("https://trabalhoindigenista.org.br/home/")'>Centro de Trabalho Indigenista</v-list-item> 
                    <v-list-item @click='open("https://www.greenpeace.org/international/")'>Greenpeace</v-list-item>                  
                  </v-list>            
                  </v-flex>
                  <v-flex v-if="getProvince == 'India'">
                  <v-list>
                    <v-card-title>How can I help?</v-card-title>
                    <v-list-item @click='open("https://www.oxfamintermon.org/")'>Oxfam Intermon</v-list-item>
                    <v-list-item @click='open("https://akshy.org")'>Akshy</v-list-item>
                  </v-list>   
                  </v-flex>               
                </v-flex>
                <v-flex v-if="isFuturo">
                  <v-card-title> 
                    What's gonna happen
                  </v-card-title>
                  <v-list v-if="getProvince == 'Congo'"> 
                    <v-card-title>
                      How can I help?
                    </v-card-title>
                    <v-list-item @click='open("https://www2.cruzroja.es")'>Unicef</v-list-item>
                    <v-list-item>Save the children</v-list-item>
                  </v-list>
                </v-flex>                                
            </v-card>
</template>

<script>
    import { mapGetters } from 'vuex';

    export default {
        data() {
            return {

            };
        },
        methods: {
          toggleHistorico() {
            this.$store.commit('toggleHistorico');
          },
          toggleActual() {
            this.$store.commit('toggleActual');
          },
          toggleFuturo() {
            this.$store.commit('toggleFuturo');
          },
          open(url) {
            window.open(url);
          },                   
        },
        computed: {
            ...mapGetters([
                'isHistorico',
                'isActual',
                'isFuturo',
                'getProvince',
                'getHazards',
            ]),
        },
    }
</script>