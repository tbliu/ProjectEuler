/// Calculate the largest prime factor of n

extern crate time;
use time::PreciseTime;

fn find_largest_prime(n : i64) -> i64 {
    let mut largest_prime : i64 = 0;
    let mut i = 2;
    let mut limit = n;
    while i * i <= limit {
        if limit % i == 0 {
            limit /= i;
            largest_prime = i;
        } else {
            i += 1;
        }
    }

    if limit > largest_prime {
        largest_prime = limit;
    }

    return largest_prime;
}

fn main() {
    let start = PreciseTime::now();
    let largest_prime = find_largest_prime(600_851_475_143);
    let end = PreciseTime::now();
    println!("{}", largest_prime);
    println!("Operation took {} seconds", start.to(end));
}
