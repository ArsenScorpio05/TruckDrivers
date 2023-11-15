function ResetForm(){
    document.getElementById('exampleDataList').addEventListener('change', function() {
    var selectedOption = this.value;
    var datalistOptions = document.getElementById('datalistOptions').getElementsByTagName('option');

    for (var i = 0; i < datalistOptions.length; i++) {
        if (datalistOptions[i].value === selectedOption) {
            document.getElementById('id_first_name').value = datalistOptions[i].getAttribute('data-first_name');
            document.getElementById('id_last_name').value = datalistOptions[i].getAttribute('data-last_name');
            document.getElementById('id_email').value = datalistOptions[i].getAttribute('data-email');
            document.getElementById('id_phone_number').value = datalistOptions[i].getAttribute('data-phone');
            document.getElementById('id_truck_license').value = datalistOptions[i].getAttribute('data-license');
            break;
        }
    }
});
    
}

function clearForm() {
    var form = document.getElementById('myForm');
    form.reset();
}


function confirmDelete() {
    const confirmDelete = confirm('\n\nAre you sure you want to delete this driver?');
    if (confirmDelete) {
        const form = document.getElementById('deleteForm');
        form.submit();
    }
}
