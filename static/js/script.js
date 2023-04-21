var count = 1;
function add(){
    if (count <= 1) {
        $(`<li><label id=${count}>input name ${count}:</label>`).insertAfter("#input0");
    } else {
        $(`<li><label id=${count}>input name ${count}:</label>`).insertAfter(`#inp${(count-1)}`);
    }
    $(`<input type='text' id='inp${count}' name='name${count}' /></li>`).insertAfter(`#${count}`);
    count ++;
}
