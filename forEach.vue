<script lang="ts">

 // Best way to wait for .forEach() to complete
  async loopOnData() {
        this.data.forEach((item, index, array) => { // loop on all data then call api depend on each record
          console.log('Data :', item);
          API.finally(() => {
            if (index === this.data.length -1){ // last iteration 
               console.log('Done --------');
            }
          });
        });
    }
  
</script>
