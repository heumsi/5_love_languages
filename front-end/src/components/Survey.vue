<template>
  <div class="container">
    <div>
      <h3>마지막 입력</h3>
      <p>통계를 위한 정보로만 활용됩니다.</p>
    </div>
    <div class="form-box">
      <b-form-group label="성별">
        <b-form-radio-group id="sex" v-model="sex" :options="sex_options"></b-form-radio-group>
      </b-form-group>
      <b-form-group label="나이">
        <b-form-select v-model="age" :options="age_options" class="age-box"></b-form-select>
      </b-form-group>
      <b-form-group label="결혼 여부">
        <b-form-radio-group
          id="marrage"
          v-model="marriage"
          :options="marriage_options"
          class="marriage-box"
        ></b-form-radio-group>
      </b-form-group>
      <b-button @click="to_result">결과 확인</b-button>
    </div>
  </div>
</template>
<script>
export default {
  name: "Survey",
  data() {
    return {
      sex: "M",
      sex_options: [{ text: "남자", value: "M" }, { text: "여자", value: "F" }],
      age: 0,
      age_options: [...Array(100).keys()],
      marriage: "single",
      marriage_options: [
        { text: "미혼", value: "single" },
        { text: "기혼", value: "married" }
      ]
    };
  },
  methods: {
    to_result() {
      this.$router.push({
        name: "result",
        params: this.$route.params
      });
    }
  }
};
</script>
<style scoped>
.form-box {
  padding: 30px 0 30px 0;
}
.age-box {
  max-width: 150px;
}
.marriage-box {
  margin-bottom: 30px;
}
</style>
