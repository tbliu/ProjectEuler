/// Calculate the sum of all multiples of 3 and 5 below n
fn multiples(n : i32) -> i32 {
    let mut sum = 0;
    let mut i = 3;
    while i < n {
        sum += i;
        i += 3;
    }

    i = 5;
    while i < n {
        sum += i;
        i += 5;
    }

    i = 15;
    while i < n {
        sum -= i;
        i += 15;
    }

    return sum;
}

fn main() {
    let sum : i32 = multiples(1000);
    println!("{}", sum);
}
