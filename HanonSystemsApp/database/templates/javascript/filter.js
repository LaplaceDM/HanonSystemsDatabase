function filter(inputID, tableID, column) {
    //pass in the id of the input box, id of table you want to search, the column to search
    // Declare variables
    var input, rows, td, i, txtValue;
    input = document.getElementById(inputID).value.toUpperCase();
    rows = document.getElementById(tableID).rows;

// Loop through all table rows, and hide those who don't match the search query
    for (i = 1; i < rows.length; i++) {
    td = rows[i].cells[column-1];
        txtValue = td.textContent.toUpperCase();
        if (txtValue.indexOf(input) != -1) {
            rows[i].style.display = "";
        } else {
            rows[i].style.display = "none";
        }
    }
}