// the all cyclomatic complexity:15

package sources

//2
func factorial(n int) int {
	if n == 0 {
		return 1
	}
	return n * factorial(n-1)
}

//1
func add(a int, b int) int {
	return a + b
}

//3
func else_if(a int, b int) int {
	if a == b {
		return a
	} else if a > b {
		return a
	} else {
		return b
	}
}

//2
func for_loop(a int, b int) int {
	var sum int
	for i := a; i <= b; i++ {
		sum += i
	}
	return sum
}

//2
func and_() bool {
	return true && false
}

//2
func or_() bool {
	return true || false
}
//3
func switch_() int {
	switch {
	case true:
		return 1
	case false:
		return 2
	}
	return 3
}
