<template>
<div class="Detalles-relative">
<div>
    <h1>{{getDetails.nombre_producto}}</h1>
  <b-card no-body class="overflow-hidden" style="max-width: 999px;">
    <b-row no-gutters>
      <b-col md="6">
        <b-card-img v-bind:src="getDetails.images" class="rounded-0"></b-card-img>
      </b-col>
      <b-col md="6">
        <b-card-body title="Horizontal Card">
          <b-card-text>
            {{getDetails.descripcion}}
          </b-card-text>
          <b-card-text>Precio Unidad:</b-card-text>
          <b-card-text>{{getDetails.precio_unidad}}</b-card-text>
          <b-card-text>Vendedor</b-card-text>

           <b-card-text>{{getProducts}}</b-card-text>
 
       
        </b-card-body>
      </b-col>
    </b-row>
  </b-card>
</div>
  
</div>
    
</template>
<script>
import { mapGetters, mapMutations} from 'vuex'
import Cartas from '@/components/Cartas.vue'
export default {
    methods:{},
    computed:{
        ...mapGetters([
            'getDetails',
            'getPath',
            'getProducts'
        ])
    },
    name: 'Detalles',
    components: {
        Cartas
    }
}
</script>
<style>

</style>
