function find_cat(my_obj) {
    let catalog = document.getElementById('list_global') //.innerHTML
    //for (let i of catalog) {
    //    console.log(i)
    //}
    let letter = my_obj.value
    for (let item of catalog.children) {
        if (item.innerHTML.includes(letter)) {
            item.style.display = 'inline';

        } else { item.style.display = 'None';
         }
    }}