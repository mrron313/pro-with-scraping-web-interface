<template>
  <div id="app">
    <h2>{{ title }}</h2>
    <form @submit="formSubmit">
      <input v-model="link" type="text" />
      <button class="btn btn-success">Submit</button>
    </form>

    <video-card v-if="success" v-bind="{videoInfo}"></video-card>
    <loading v-if="loading"></loading>
  </div>
</template>

<script>
export default {
  name: "app",
  data() {
    return {
      title: "How to Become a Pro with Scraping Youtube Videos in 3 minutes",
      link:
        "https://www.youtube.com/watch?v=9XvXF1LrWgA&list=RDAY0VGbNbkcc&index=3",
      videoInfo: {
        category: "",
        likes: "",
        dislikes: "",
        published: "",
        thumbnail: "",
        title: "",
        views: ""
      },
      success: false,
      loading: false
    };
  },
  methods: {
    formSubmit(e) {
      e.preventDefault();
      this.success = false;
      this.loading = true;
      this.$http
        .post("http://127.0.0.1:5000/extract-utube-info", this.link, {
          headers: {
            "Content-Type": "text/plain"
          }
        })
        .then(response => {
          this.videoInfo = response.data;
          this.success = true;
          this.loading = false;
        })
        .catch(error => {
          this.success = false;
          this.loading = false;
        });
    }
  }
};
</script>

<style>
body {
  background-color: #263859;
}

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #bbe1fa;
  margin-top: 60px;
}

h2 {
  color: #ff6768;
}

input[type="text"] {
  width: 47%;
  padding: 7px 19px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

button {
  display: inline-block;
  font-weight: 400;
  color: #ffffff;
  text-align: center;
  vertical-align: middle;
  cursor: pointer;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  background-color: #ff6768;
  border: 1px solid transparent;
  padding: 0.375rem 0.75rem;
  font-size: 0.75rem;
  line-height: 1.5;
  border-radius: 0.25rem;
}
</style>
