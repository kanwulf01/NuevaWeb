<template>
<div>
  <div class="container" >
       
    <b-card-group deck >
       <b-card   v-for="(i,index) in trae" v-bind:index="index"  v-if="index < 4" :key="i.id" bg-variant="secondary" text-variant="white" header="NeuroMarket" class="text-center mb-2"
      
   
    img-alt="Image"
    img-top
    tag="article"
    style="max-width: 20rem;">
    <form v-on:submit.prevent="Getid(i)">
      
        <b-card-title>{{i.nombre_producto}}</b-card-title>
        <b-card-img v-bind:src="i.images" fluid alt="Fluid image"></b-card-img>
       <b-card-text>Compralo Ahora!</b-card-text>
        <button class="btn btn-success" >Detalles</button>
    </form>
      </b-card>
    </b-card-group>

    <b-card-group deck >
       <b-card   v-for="(j,index) in trae2" v-bind:index="index" v-if="index < 4" :key="j.id" bg-variant="secondary" text-variant="white" header="NeuroMarket" class="text-center mb-2"
      
   
    img-alt="Image"
    img-top
    tag="article"
    style="max-width: 25rem;">
    <form v-on:submit.prevent="Getid(j)">
        <b-card-title>{{j.nombre_producto}}</b-card-title>
        <b-card-img v-bind:src="j.images" fluid alt="Fluid image"></b-card-img>
        <b-card-text>Compralo Ahora!</b-card-text>
        <button class="btn btn-success">Detalles</button>
    </form>
      </b-card>
    </b-card-group>
  </div>
  
</div>
</template>
<script>
let data = [1,2,3,4]
import { mapGetters, mapMutations} from 'vuex'
export default {
  methods:{
    ...mapMutations([
      'setDetalle',
      'setCount'
    ]),
      Getid(i){
        this.setDetalle(i)
        this.setCount(i)
        this.$router.push({path:'/Details'})
      }
     
    },
computed:{
  ...mapGetters([
    'getProducts',
    'getCount'
    
  ]),trae(){
      return this.getProducts
      alert('prueba1'+this.getProducts)
    },
    trae2(){
      return this.getCount
    }
    
      
     
    }
   
}
</script>
<style >

</style>
