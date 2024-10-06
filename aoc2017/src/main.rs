use std::fs::read_to_string;

fn main() {
    one();
    two();
}

fn two() {
    let mut total: u32 = 0;
    let mut sum: u32 = 0;
    for _ in read_to_string("src/input.txt").unwrap().chars() {
        total += 1;    
    }

    let half:u32 = total / 2;
    let nums_in_str: String  = read_to_string("src/input.txt").unwrap().to_string();

    let mut index:u32 = 0;
    for char in read_to_string("src/input.txt").unwrap().chars() {
        if index >= half {
            break
        }

        let compare_to_index:u32 = half + index; 
        let ch= nums_in_str.chars().nth(compare_to_index as usize).unwrap();

        if ch == char {
            sum += char.to_digit(10).unwrap();
        }
        index += 1;        
    }   
    println!("problem 2 : {}", sum * 2);
}


fn one() {
    let mut sum = 0;
    let mut last_num = 0;
    for char in read_to_string("src/input.txt").unwrap().chars() {
        
        let number : u32 = char.to_digit(10).unwrap();

        if last_num == number {
            sum = sum + number;
        }
        last_num = number;
    }

    println!("Problem 1 : {}", sum.to_string());
}

