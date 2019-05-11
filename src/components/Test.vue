<template>
    <div class="container" st>
        <b-button-group class="a" vertical>
            <div>{{no+1}} / {{questions.length}}</div>
            <b-button @click="next(0)">{{questions[no][0]['statement']}}</b-button>
            <b-button @click="next(1)">{{questions[no][1]['statement']}}</b-button>
        </b-button-group>
    </div>
</template>

<script>
import questions from '@/assets/questions.json'
export default {
    name: "Test",
    data () {
        return {
            "questions": questions,
            "no": 0,
            "result": {
                "A" : 0,
                "B" : 0,
                "C" : 0,
                "D" : 0,
                "E" : 0
            }
        }
    },
    methods: {
        next(answer_idx) {
            let answer_type = this.questions[this.no][answer_idx]['type']

            this.result[answer_type] += 1
            this.no += 1

            if (this.no >= 30) {
                this.$router.push({
                    name: 'result',
                    params: this.result
                })
            }
        }
    },
}
</script>


<style scoped>
.container {
    
}
.a {
    width: 100%;
}
</style>
