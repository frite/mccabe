// the all cyclomatic complexity:18
//2
function factorial(n) {
    if (n === 0) {
        return 1
    }
    return n * factorial(n - 1)
}

//1
function add(a, b) {
    return a + b
}

//3
function elseif(a) {
    if (a === 0) {
        return 0
    } else if (a === 1) {
        return 1;
    }
}

//2
function for_() {
    for (let i = 0; i < 1; i++) {

    }
}

//2
function while_() {
    while (1) {
        return
    }
}

//2
function try_() {
    try {

    } catch (e) {

    }
}

//2
function with_() {
    with (1) {

    }
}

//2
function and_() {
    return 1 && 2
}

//2
function or_() {
    return 1 || 2
}
