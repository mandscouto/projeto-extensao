/* var resposta = confirm("Deseja excluir?");
console.log(resposta); */
const a = 10;
const b = 33;
function somar(a, b){
    return a + b;
}
//console.log(somar(2,5));

document.querySelector("#calcular").addEventListener("click", function(){
    let valorA = document.querySelector("valorA");
    let valorB = document.querySelector("valorB");
    alert(parseInt(valorA)+parseInt(valorB));
});