function makeGraph(data,divId){
   return $.plot(divId, [ data ], {
      grid: {
      hoverable: true
      },
      series: {
bars: {
show: true,
barWidth: 0.6,
align: "center"
}
},
xaxis: {
mode: "categories",
tickLength: 0
}
});
}
function addToGraph(plot,data){
  plot.setData([data]);
  plot.setupGrid();
  plot.draw();
}
 

function makeWeaponGraph(user){
 var wplot = makeGraph([[]],"#wepgraph");
$.ajax({
type: "GET", 
async: true,
url:"/weapon_deaths/"+user+"&1000",
dataType:"json",
success: 
function(data){
  var gData = data;
  addToGraph(wplot,gData);
  },
error: function(request, errorText, errorCode){alert(errorText);} });



}
