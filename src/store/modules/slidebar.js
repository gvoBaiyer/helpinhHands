import Axios from 'axios';
export default {
    state: {
        historico: false,
        actual: true,
        futuro: false,
        province: null,
        slides: [
            'Dozens Dead after Typhoon Hagibis Hits Central and Eastern Japan',
            'Earthquake in Pakistani Kashmir leaves dozens dead',
            'Kurdish forces agree to withdraw from Turkey-Syria border',
            'Alarming Child Poverty Risk In Spain Despite The Economic Recovery',
            'World hunger is still not going down after three years and obesity is still growing',
        ],
        hazards: null,
        news: null,
        country: null
    },
    getters: {
        isHistorico: state => state.historico,
        isActual: state => state.actual,
        isFuturo: state => state.futuro,
        getProvince: state => state.province,
        getSlides: state => state.slides,
        getHazards: state => state.hazards,
        getNews: state => state.news,
    },
    mutations: {
        toggleHistorico(state) {
            state.historico = true;
            state.actual = false;
            state.futuro = false;
        },
        toggleActual(state) {
            state.historico = false;
            state.actual = true;
            state.futuro = false;
        },
        toggleFuturo(state) {
            state.historico = false;
            state.actual = false;
            state.futuro = true;
        },
        setProvince(state, province) {
            state.province = province;
        },
        setHazards(state, hazards) {
            state.hazards = hazards;
        },
        setNews(state, news) {
            state.news = news;
        },
    },
    actions: {
        setCountry: ({ commit }, country) => new Promise((resolve, reject) => {
            Axios.get(`http://localhost:5000/hazards?country=${country}`).then((response) => {
                commit('setHazards', response.data);
                resolve(response);
            })
            .catch((error) => {
                reject(error);
            });
        }),
        setNews: ({ commit }, country) => new Promise((resolve, reject) => {
            let url = 'http://localhost:5000/news';
            if (country) {
                url += '?country=' + country.toLowerCase()
            }
            Axios.get(url).then((response) => {
                commit('setNews', response.data.articles);
                resolve(response);
            })
            .catch((error) => {
                reject(error);
            });
        }),        
    },
}