const data = require("./dados.json");

let dados = JSON.stringify(data)
dados = JSON.parse(dados)
let lista = [];
let i;

for (i in dados){
    if (dados[i].valor != 0.0){
        lista.push(dados[i].valor);
    }
}

let min = Math.min(...lista);
let max = Math.max(...lista);

let sum = 0.0;

for (let i = 0; i < lista.length; i++) {
    sum += lista[i];
}

let media = sum/lista.length;
let lista2 = [];
for(i = 0; i < lista.length; i++){
    if(lista[i] > media){
        lista2.push(lista[i]);
    }
}

console.log(`O menor valor de faturmento diário do mês foi de R$ ${min}`);
console.log(`O maior valor de faturmento diário do mês foi de R$ ${max}`);
console.log(`O número de dias em que o faturamento foi maior que a média mensal foi de ${lista2.length} dias`);