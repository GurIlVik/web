var sitys = []

function unloud_html () {
    let string = document.getElementById("memory").innerText;
    let result = ''
    for (let i = 0; i<string.length; i++) {
        if (string[i] != ','){
            result += string[i];
        } else {
            sitys.push(result);
            result = '';
        }
    }
}


let sity_comp = '';
let list_sity_post = [];

function nachalo () {
    unloud_html ();
    document.getElementById('s3').innerHTML = 'любую';
    document.getElementById('s1').innerHTML = "ваш ход";
    document.getElementById('s2').innerHTML = "";
    }


function collect_a_list () {
    let result = '';
    let i = 0;
    for (i = 0; i<list_sity_post.length; i ++) {
        if ("Ты выиграл!" != list_sity_post[i]) {
        result += list_sity_post[i]+',';}
    }
    document.getElementById("memory").innerHTML = result;
    list_sity_post = [];
    sity_comp = '';
    sitys = [];
}


function global_list () {
    let i;
    let res = [];
    for (i=0; i<sitys.length; i++){
        res.push(sitys[i])
    }
    for (i=0; i<list_sity_post.length; i++){
        res.push(list_sity_post[i])
    }
    return res
}


function last_letter (word) {
    let letters_no = ['ь', 'ы'];
    for (let i = 0; i < letters_no.length; i ++) {
        if (word[word.length -1] == letters_no[i]) {
            return word[word.length - 2]
        }
    }
    return word[word.length -1]
}

function check_new_sity(sity_new) {
    let i;
    let chek = 0;
    let sit_list = global_list ();
    if ('Этот город уже был, введите другой.' != sity_new) {
    for (i = 0; i < sit_list.length; i ++){
        if (sity_new == sit_list[i]) {
            chek += 1; }}   
    if (chek != 1) {
        document.getElementById('s2').innerHTML += '<br>' + "Спасибо, я добавил в свой список новый город!";
    }}}


function get_next_city(my_city) {
	for (var i = 0; i < sitys.length; i++) {
		if (sitys[i][0].toLowerCase() === last_letter(my_city)) {
            if (sitys[i] != my_city) {
			let result = sitys[i];
			sitys = sitys.filter( item => item !== result);
			return result;
		}}
	}
    for (let i = 0; i < sitys.length; i++) {
        list_sity_post.push(sitys[i]);
    }
	return "Ты выиграл!"
}

function writer (sity_comp, sity_user) {
    document.getElementById('s1').innerHTML = sity_comp;
    document.getElementById('s3').innerHTML = last_letter(sity_comp);
    document.getElementById('s2').innerHTML += '<br>' + sity_user + " - " +  sity_comp;
    list_sity_post.push(sity_user);
    list_sity_post.push(sity_comp);
    sitys = sitys.filter(item => item !== sity_user);
    document.getElementById('a1').value = ''; // почему не работает innerHTML 
    if ("Ты выиграл!" == sity_comp) {
        let blok_finish = document.getElementById('finish');
        let button_finish = document.createElement("INPUT");
        button_finish.setAttribute("type", "button", 'id = restart');
        button_finish.value = "Начать снова";
        button_finish.style.backgroundColor = '#e7ef10';
        button_finish.style.width = '24vw';
        button_finish.style.height = '6vw';
        button_finish.style.fontSize = '3vw';
        button_finish.style.color = '#263ec4';
        button_finish.style.borderRadius = '70%';
        blok_finish.appendChild(button_finish);
        button_finish.onclick = function() {
            sity_comp = '';
            collect_a_list ();
            blok_finish.removeChild(button_finish);
            start ();
        }
    }
}

function checkuser (use) {
    let letters = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Э', 'Ю', 'Я'];
    for (let i = 0; i < letters.length; i ++) {
        if (use[0] === letters[i]) {
            for (let j = 0; j < list_sity_post.length; j ++) {
                if (list_sity_post[j] == use){
                    return 'Этот город уже был, введите другой.'}}
            return use
        }};  return false}

function start () {
    nachalo ();
    b1.onclick = function() {
        var sity_user = document.getElementById('a1').value;
        sity_user = checkuser(sity_user);
        check_new_sity(sity_user);
        if (sity_user === false) {
            
            // document.body.style["background"] = "red"; -- ОБРАЩЕНИЕ К БОДИ
            document.getElementById('s2').innerHTML += '<br>' + 'Введите правильно город, первая буква указана не верно:';
            document.getElementById('a1').value = '';
        } else {
            if (sity_user == 'Этот город уже был, введите другой.') {
                document.getElementById('s2').innerHTML += '<br>' + sity_user
            } else {
            if (sity_comp === '') {
                sity_comp = get_next_city(sity_user)
                writer (sity_comp, sity_user)
            } else {
            if (sity_comp[sity_comp.length - 1] !== sity_user[0].toLowerCase() ) {
                document.getElementById('s2').innerHTML += '<br>' + 'Введите правильно город'
            } else {
                sity_comp = get_next_city(sity_user);
                writer (sity_comp, sity_user);
               
        }}}};}
        }
    
window.onload = () => {start ();}