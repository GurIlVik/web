


function article() {
    console.log('kjwdhbv');
    let global = document.getElementById('alternativ_global');
    // let div_main = document.createElement('div');
    // console.log(global);
    global.style.display = 'block';
    // div_main.style.top = '7%'
    // div_main.style.left = '7%'
    // div_main.position = 'flex';
    // div_main.style.height = '600px';
    // div_main.style.width = '600px';
    // div_main.style.zIndex = '1';
    // div_main.style.background = 'c0c4ac79';
    // global.appendChild(div_main);
    // div_main.value = 'ewfpijnvowirnv';
    // global.innerHTML = `<p><span>&ensp;&ensp;</span><span class="Child_main_menu2">irbnwlrbvlwrbv</span><span>,</span></p> `


}


function infoUser() {
    console.log('kjwwfvwvfdhbv');
    let global2 = document.getElementById('alternativ_form_div');
    global2.style.display = 'block';
    let global3 = document.getElementById('alternativ_form_div1');
    global3.style.display = 'flex';
}

function infoUser1() {
    console.log('1-1');
    let block1 = document.getElementsByClassName('alternativ_form_div');
    console.log(block1)
    for (let i = 0; i<block1.length; i ++) {
        console.log(block1[i])
        block1[i].style.display = 'none';
    }
    let global2 = document.getElementById('form_use1');
    global2.style.display = 'flex';
    let global3 = document.getElementById('p_inf_write');
    global3.style.display = 'block';
}

function viborPredmet(){
    console.log('1-3')
    let blok2 = document.getElementById('alternative_global_3');
    blok2.style.display = 'block';
    blok2.style.zIndex = '10';
}


// разрисовывание функции объектов
function menuPoint20(object) {
    console.log(object.id);
    let list_object = [];
    let value_list = document.getElementsByClassName("Child_main_menu2")
    for (let item of value_list) {
        list_object.push(item.textContent)
        }
    console.log(list_object);
    key = control_word (list_object, object.id)
    if (key == false) {
        let div_object = document.getElementById('plusPredmet');
        let div_object2 = document.getElementById('id_interest');
        div_object2.style.zIndex = '-1000'
        div_object.innerHTML += `<p><span>&ensp;&ensp;</span><span class="Child_main_menu2">${object.id}</span><span>,</span></p> `
        div_object2.innerText += '${object.id}'
        list_object.push(object.id)
        console.log(list_object);
        let object_id2 = object.id + ', '
        console.log('value kukuk156', object.id);
        div_object2.value += object_id2;
        console.log(list_object);
        console.log(div_object2);
        // find_cat('')
    } 
}

// сброс выбранных параметров во 2 меню
function menuPoint25() {
    let value_list = document.getElementById('plusPredmet');
    value_list.innerHTML = `<p>Предмет коллекционирования:</p>`
    console.log(value_list.innerText)
    let div_object2 = document.getElementById('q1');
    div_object2.value = ''
    div_object2.style.zIndex = '-10'
    console.log(div_object2.value);
}

function menuPoint24() {
    let block = document.getElementById('alternative_global_3');
    block.style.display = 'none';
}

// ввод меню для добавления элемента
function menuPoint23() {
    viborPredmet();
    let catalog = document.getElementById('list_global');
    catalog.style.display = 'flex'
    catalog.style.flexDirection = 'row';
    catalog.style.alignContent = 'space-around';
    for (let item of catalog.children) {
        item.style.display = 'flex'
        }
}

// проверка на дублирование во втором меню
function control_word (list_object, object) {
    let lis_ob_li = list_object.length;
    key = false;
    for (let i = 0; i <= lis_ob_li; i +=1) {
        console.log(list_object[i]);
        console.log(typeof(list_object[i]));
        console.log(object);
        console.log(typeof(object));
        if (list_object[i] == object) {
            key = true;
            return key
        } 
    }
    return key
}

function find_cat(my_obj) {
    let catalog = document.getElementById('list_global') //.innerHTML
    let letter = my_obj.value
    for (let item of catalog.children) {
        if (item.innerHTML.includes(letter)) {
            item.style.display = 'inline';
        } else { item.style.display = 'None';
         }
    }}


function infoUser2(inf) {
    console.log('1-1');
    let global2 = document.getElementById(inf);
    global2.style.display = 'flex';
}

function clouseWin(win1) {
    console.log('lweibhv')
    let global1 = document.getElementById("alternativ_form_div");
    let global2 = document.getElementById("alternativ_form_div1");
    global2.style.display = 'none';
    global1.style.display = 'none';
}

function redaction() {
    console.log('lewfnhliewruhrveio2u')
}