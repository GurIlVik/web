



function article() {
    let global = document.getElementById('alternativ_global');
    global.style.display = 'block';
}


function infoUser() {
    let global2 = document.getElementById('alternativ_form_div');
    global2.style.display = 'block';
    let global3 = document.getElementById('alternativ_form_div1');
    global3.style.display = 'flex';
}

function infoUser1() {
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
    let div_object2 = document.getElementById('id_interest');
    div_object2.value = ''
    console.log(div_object2)
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
    let global2 = document.getElementById(inf);
    global2.style.display = 'flex';
}

function clouseWin(win1) {
    let global1 = document.getElementById("alternativ_form_div");
    let global2 = document.getElementById("alternativ_form_div1");
    global2.style.display = 'none';
    global1.style.display = 'none';
}

function redaction(art) {
    let div_info = document.getElementById('id_for_form_'+art);
    let div_info_title = document.getElementById('key_title_id_'+art);
    let div_info_text = document.getElementById('key_text_id_'+art);
    article();
    let div_form_topic = document.getElementById('pu_div21');
    let div_form_categories = document.getElementById('pu_div22');
    let div_form_allowance = document.getElementById('pu_div23');
    let div_form_photo = document.getElementById('pu_div24');
    let div_form_title = document.getElementById('id_title');
    let div_form_text = document.getElementById('id_text');
    let title = div_info_title.innerText;
    console.log(title)
    let text = div_info_text.innerText;
    console.log(text)
    div_form_title.value = title
    div_form_text.value = text
    let button_memory = document.getElementById('non_id_memory');
    button_memory.name = 'memor_'+art
    let button_write = document.getElementById('non_id_write');
    button_write.name = 'writ_'+art
    let button_delete = document.getElementById('non_id_delete');
    button_delete.name = 'delet_'+art

}

// Фуекции всплывающего окна и его закрытия
function fun_foto(param) {
    let block = param;
    console.log(param.src)
    let block2 = document.getElementById('info_blok_90');
    block2.style.display = 'block';
    let block3 = document.getElementById('info_blok_91');
    block3.style.display = 'block';
    console.log('lwrjbhglkwrjtbgwlrijb')
    let block5 = document.createElement('img');
    block5['src'] = param.src;
    console.log(block5)
    block5['class'] = 'img_for_arts';
    block2.appendChild(block5);
}
function clouse_photo() {
    let block2 = document.getElementById('info_blok_90');
    let block3 = document.getElementById('info_blok_91');
    block2.style.display = 'none';
    block3.style.display = 'none';
}







// Итак в чём же основная проблема с которой столкнулся я. Оказывается “выключить” кнопку можно как угодно, т.е. обратившись к элементу submit в любой доступной форме:
// Submit.disabled = true;
// Однако включить (заменим на false) подобным способом не получается и именно поэтому я накопал аж вот такую конструкцию:
// Document.form_del.elements["submit"].disabled = true;
// И вот здесь, если мы заменям true на false, то кнопка как включается, так и выключается. Ну и напоследок расшифрую я эту строчку кода:
// В теущем документе в форме по имени “form_del” в элементе у которого имя “submit” (а у нас в примере это имя носит кнопка) есть свойсто “disabled”, так вот мы включаем его “true” или выключаем “false”. Т.о. включив данное свойство мы сделаем нашу кнопку неактивной, а выключив свойство, наша кнопка снова станет активной.
// ) ставился вопрос о том, что было бы хорошо кнопкам формы, отправляемой на сервер, ставить свойство disabled = "disabled" .
// Однако, до сих пор так и не разобрались, зачем это нужно и как все-таки это делать. Казалось бы, что может быть проще и о чем здесь вообще можно разговаривать, ан нет - на поверку все оказалось не так тривиально. Сразу замечу, что нижеследующие рассуждения применимы к обеим типам форм: как отправляемым через обычный SUBMIT, так и с помощью AJAX.



