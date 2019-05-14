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
      <b-button variant="primary" 
        :disabled="isValid"
        @click="to_result">결과 확인</b-button>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "Survey",
  data() {
    return {
      sex: null,
      sex_options: [{ text: "남자", value: "M" }, { text: "여자", value: "F" }],
      age: null,
      age_options: [...Array(100).keys()],
      marriage: null,
      marriage_options: [
        { text: "미혼", value: "single" },
        { text: "기혼", value: "married" }
      ],
    };
  },
  computed: {
    isValid() {
      return this.sex == null || this.age == null || this.marriage == null
    }
  },
  methods: {
    to_result() {
      // calculate top3 type of user.
      let score = this.$route.params
      let type_name_sorted = Object.keys(score);    
      type_name_sorted.sort((a, b) => {return score[b] - score[a]});
      let top = type_name_sorted.slice(0, 3)

      // make result object.
      let result = score
      for (var i in top) {
        result["top"+i] = top[i]
      }
      result['sex'] = this.sex
      result['age'] = this.age
      result['marriage'] = this.marriage
      result['timestamp'] = Date.now()

      // insert result into DB. 
      axios.post('http://localhost:5000/addResult', result)
      console.log(result)

      // redirect into result page.
      this.$router.push({
         name: "result",
         params: score
      });
    },
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
