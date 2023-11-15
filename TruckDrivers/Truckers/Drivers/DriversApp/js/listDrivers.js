document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const driverList = document.getElementById('driverList');
    const drivers = driverList.getElementsByTagName('li');

    searchInput.addEventListener('keyup', function() {
        const searchText = searchInput.value.toLowerCase();

        for (let i = 0; i < drivers.length; i++) {
            const driverName = drivers[i].textContent.toLowerCase();
            if (driverName.includes(searchText)) {
                drivers[i].style.display = 'block';
            } else {
                drivers[i].style.display = 'none';
            }
        }
    });
});
