import Vue from 'vue'
import Vuex from 'vuex'

import slidebars from './modules/slidebar';

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    slidebars,
  },
});
