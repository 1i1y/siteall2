

        $(function () {
	
            var map = new GMaps({
                el: "#map1",
                 lat:  lat[0],
				lng: lng[0],
                zoom: 10,
                zoomControl : true,
                zoomControlOpt: {
                    style : "SMALL",
                    position: "TOP_LEFT"
                },
                panControl : true,
                streetViewControl : false,
                mapTypeControl: false,
                overviewMapControl: false
            });

            var styles = [
                {
                    stylers: [
                        { hue: "#00ffe6" },
                        { saturation: -2 }
                    ]
                }, {
                    featureType: "road",
                    elementType: "geometry",
                    stylers: [
                        { lightness: 100 },
                        { visibility: "simplified" }
                    ]
                }, {
                    featureType: "road",
                    elementType: "labels",
                    stylers: [
                        { visibility: "off" }
                    ]
                }
            ];
            
            map.addStyle({
                styledMapName:"Styled Map",
                styles: styles,
                mapTypeId: "map_style"
            });

            map.setStyle("map_style");
        });
        function test(loc){ 
		var map = new GMaps({
            el: "#map1",
            lat:  lat[loc],
            lng: lng[loc],
            zoom: 10,
            zoomControl : true,
            zoomControlOpt: {
                style : "SMALL",
                position: "TOP_LEFT"
            },
            panControl : true,
            streetViewControl : false,
            mapTypeControl: false,
            overviewMapControl: false
        });
            map.addMarker({
                lat: lat[loc],
                lng: lng[loc],
                title: 'Lima',
                click: function(e) {
                    alert('You clicked in this marker');
                }
            });
            var styles = [
                {
                    stylers: [
                        { hue: "#00ffe6" },
                        { saturation: -2 }
                    ]
                }, {
                    featureType: "road",
                    elementType: "geometry",
                    stylers: [
                        { lightness: 100 },
                        { visibility: "simplified" }
                    ]
                }, {
                    featureType: "road",
                    elementType: "labels",
                    stylers: [
                        { visibility: "off" }
                    ]
                }
            ];

            map.addStyle({
                styledMapName:"Styled Map",
                styles: styles,
                mapTypeId: "map_style"
            });

            map.setStyle("map_style");
        };