l = [1,2,3,4,5,6,7,8,9,10];
for (i = 0; i < l.length -1; i+=2) {
    tmp = l[i];
    l[i] = l[i+1];
    l[i+1] = tmp;
}

debugger;