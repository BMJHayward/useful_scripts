function mergesort(array){
    if (array.length > 1){
        var mid = Math.floor(array.length/2);
        lefthalf = array.slice(0, mid);
        righthalf = array.slice(mid, array.length);
        mergesort(lefthalf);
        mergesort(righthalf);
        var i = 0; var j = 0; var k = 0;
        while (i<lefthalf.length && j<righthalf.length){
            if (lefthalf[i] < righthalf[j]){
                array[k] = lefthalf[i];
                i++;
            } else {
                array[k] = righthalf[j];
                j++;
            }
            k++;
        }
        while (i<lefthalf.length){
            array[k] = lefthalf[i];
            i++; k++;
        }
        while (j<righthalf.length){
            array[k] = righthalf[j];
            j++; k++;
        }
    }
};
var testdata = [];
for (var l=0; l<10; l++){
    testdata.push(Math.floor(Math.random()*10));
};
mergesort(testdata);
