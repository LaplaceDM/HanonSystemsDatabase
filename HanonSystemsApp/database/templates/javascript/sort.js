        function sort_num(tableID, column, ascending){
            //pass in the id of the table to sort, the position of the column to sort in order
            //from left to right, boolean true for ascending order, false for descending order
            var rows = document.getElementById(tableID).rows;
            var arr=[];

            for (i=1; i<rows.length; i++){
                arr[i-1] = rows[i];
            }
            var sortedArr = sorter_num(arr, column-1, ascending);
            rearrangeTable(tableID, sortedArr);
        }

        function sort_str(tableID, column, alphabet){
            //pass in the id of the table to sort, the position of the column to sort in order
            //from left to right, boolean true for alphabetical order, false for reverse alphabetical order
            var rows = document.getElementById(tableID).rows;
            var arr=[];

            for (i=1; i<rows.length; i++){
                arr[i-1] = rows[i];
            }
            var sortedArr = sorter_str(arr, column-1, alphabet);
            rearrangeTable(tableID, sortedArr);
        }

        function sorter_num(arr, column, ascending) {
            // Base case
        if (arr.length <= 1) {
            return arr;
        }
        var mid = Math.floor(arr.length / 2);
        // Recursive calls
        var left = sorter_num(arr.slice(0, mid), column, ascending);
        var right = sorter_num(arr.slice(mid), column, ascending);
        return merge_num(left, right, column, ascending);
        }

        function merge_num(left, right, column, ascending) {
        var sortedArr = []; // the sorted items will go here
        if (ascending){
            while (left.length && right.length) {
            // Insert the smallest item into sortedArr
                if (parseInt(left[0].cells[column].innerHTML) < parseInt(right[0].cells[column].innerHTML)) {
                    sortedArr.push(left.shift());
                } else {
                    sortedArr.push(right.shift());
                }
            }
        // Use spread operators to create a new array, combining the three arrays
            return [...sortedArr, ...left, ...right];
        }
        else{
            while (left.length && right.length) {
            // Insert the largest item into sortedArr
                if (parseInt(left[0].cells[column].innerHTML) > parseInt(right[0].cells[column].innerHTML)) {
                    sortedArr.push(left.shift());
                } else {
                    sortedArr.push(right.shift());
                }
            }
            return [...sortedArr, ...left, ...right];
        }
    }

        function rearrangeTable(tableID, arr) {
            var table = document.getElementById(tableID);
            for (i=0; i<arr.length; i++){
                table.appendChild(arr[i]);
            }
        }


        function sorter_str(arr, column, alphabet) {
            // Base case
        if (arr.length <= 1) {
            return arr;
        }
        var mid = Math.floor(arr.length / 2);
        // Recursive calls
        var left = sorter_str(arr.slice(0, mid), column, alphabet);
        var right = sorter_str(arr.slice(mid), column, alphabet);
        return merge_str(left, right, column, alphabet);
        }

        function merge_str(left, right, column, alphabet) {
        var sortedArr = []; // the sorted items will go here
        if (alphabet){
            while (left.length && right.length) {
            // Insert the smallest item into sortedArr
                if ((left[0].cells[column].innerHTML).localeCompare(right[0].cells[column].innerHTML)==-1) {
                    sortedArr.push(left.shift());
                } else {
                    sortedArr.push(right.shift());
                }
            }
        // Use spread operators to create a new array, combining the three arrays
            return [...sortedArr, ...left, ...right];
        }
        else{
            while (left.length && right.length) {
            // Insert the largest item into sortedArr
                if ((left[0].cells[column].innerHTML).localeCompare(right[0].cells[column].innerHTML)==1) {
                    sortedArr.push(left.shift());
                    console.log(sortedArr[sortedArr.length-1]);
                } else {
                    sortedArr.push(right.shift());
                    console.log(sortedArr[sortedArr.length-1]);
                }
            }
            return [...sortedArr, ...left, ...right];
        }
    }