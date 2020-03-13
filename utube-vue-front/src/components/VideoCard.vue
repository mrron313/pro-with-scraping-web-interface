<template>
  <div class="video-card">
    <h4>{{ videoInfo.title }}</h4>
    <div class="video-details">
      <div class="video-img">
        <img width="250" height="150" :src="imageSrc(videoInfo.thumbnail)" />
      </div>
      <div class="video-info">
        <ul>
          <li>{{ videoInfo.category }}</li>
          <li>{{ videoInfo.published }}</li>
          <li>{{ videoInfo.views }}</li>
          <li>{{ videoInfo.likes }} likes</li>
          <li>{{ videoInfo.dislikes }} dislikes</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: { videoInfo: { type: Object, required: false } },
  methods: {
    imageSrc: function(img) {
      return img;
    }
  }
};
</script>

<style>
.video-card {
  margin: 0px auto;
  width: 80%;
}

.video-card h4 {
  color: #eae7af;
}

.video-details {
  display: flex;
  flex-direction: row;
  justify-content: center;
}

.video-info {
  padding: 14px 8px;
}

.video-info ul {
  margin: 0;
  padding-left: 10px;
  text-align: left;
}

.video-info ul li {
  padding-bottom: 7px;
  list-style: none;
}
</style>