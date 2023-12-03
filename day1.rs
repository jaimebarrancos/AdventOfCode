use std::fs::read_to_string;


fn getNumbers() {
    let mut sum = 0;

    for line in read_to_string("src/input.txt").unwrap().lines() {
 
        let mut number = 0;
        for letter in line.chars() {
            if letter.is_numeric(){
                let no: u32 = letter.to_digit(10).unwrap();

                if number == 0 {
                    number = no + 10*no;
                }
                else {
                    number =  no + number/10 * 10;
                }
            }
        }
        sum = sum + number;
    }
    println!("Result:  {}",   sum.to_string());

  }