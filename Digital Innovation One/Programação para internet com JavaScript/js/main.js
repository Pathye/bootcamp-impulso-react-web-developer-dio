/*
function soma(n1, n2){
    return n1 + n2;
}

alert(soma(5, 10));

var validar = 0;
function validaIdade(idade){
    if (idade >= 18){
        validar = true;
    }
    else{
        validar = false;
    }
    return validar;
}

var idade = prompt("Qual sua idade?");
validaIdade(idade)
console.log(validar);
*/

function clicou(){
    document.getElementById("thankyou").innerHTML = "<b>Obrigado por clicar</b>";
    // alert("Você clicou no botão");
}

function trocar(Elemento){
    // document.getElementById("trocar").innerHTML = "Mágica, apenas mágica!";
    Elemento.innerHTML = "Mágica, apenas mágica!";
}

function voltar(Elemento){
    // document.getElementById("trocar").innerHTML = "Passe o mouse aqui";
    Elemento.innerHTML = "Passe o mouse aqui";
}

/*
function setReplace(frase, nome, novo_nome){
    return frase.replace(nome, novo_nome)
}

alert(setReplace("País: Japão", "Japão", "Brasil"));
*/