import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import VideoCard from './components/VideoCard.vue'
import Loading from './components/Loading.vue'

Vue.prototype.$http = axios

Vue.component('video-card', VideoCard)
Vue.component('loading', Loading)

new Vue({
  el: '#app',
  render: h => h(App)
})
