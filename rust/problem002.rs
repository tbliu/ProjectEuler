/// Calculate the sum of even numbers in the fibonacci sequence up to n
/// Fibonacci sequence starts with 1 and 2

fn sum_even_fib(n : i32) -> i32 {
    let mut v1 = 1;
    let mut v2 = 2;
    let mut curr = 0;
    let mut sum = 0;
    if n >= 2 {
        sum = 2;
    }

    while curr < n {
        curr = v1 + v2;
        if curr % 2 == 0 {
            sum += curr;
        }
        let temp = curr;
        v1 = v2;
        v2 = temp;
    }

    return sum;
}

fn main() {
    let sum : i32 = sum_even_fib(4_000_000);
    println!("{}", sum);
}
