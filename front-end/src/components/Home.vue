<template>
  <div>
    <b-jumbotron>
      <template slot="header">사랑의 5가지 언어</template>

      <template s lot="lead">
        사랑은 언어처럼 많은 뉘앙스를 가지고 있습니다.
        <br>1995 년, 게리 채프먼은 그가 존재한다고 믿는 5가지 사랑에 관한 언어를 설명했다. 그는 사람이 사랑을 표현하는 방식과, 그것을 받는 방식을 모두 포함하여 설명하고자 했다.
      </template>

      <hr class="my-4">

      <p>당신의 사랑의 5가지 언어. 지금 바로 검사를 통해 확인해보세요.</p>

      <b-button variant="outline-primary" to="/test">검사 하기</b-button>
    </b-jumbotron>
  </div>
</template>
<script>
export default {
  name: "Home"
};
</script>
<style scoped>
.jumbotron {
  height: 600px;
  margin-bottom: 0;
  color: black;
  /*background-image: url("http://gagmagazine.co.kr/wp-content/uploads/2017/05/2017-05-26-10.19.56.png");*/
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
</style>
