

Vue.createApp({
            data: function () {
                return {
                    plants: []
                }
            },

            mounted: async function() {
                this.plants =await getPlant();
                console.log( await this.plants);
            }

        }).mount('#plantTable')