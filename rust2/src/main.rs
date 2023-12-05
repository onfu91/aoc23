use std::fs;

fn get_first_digit(input: &str) -> String {
    // Find the first digit in the string
    let first_digit = input.chars().find(|c| c.is_digit(10));

    // Handle the result
    match first_digit {
        Some(digit) => digit.to_string(),
        None => "".to_string(),
    }
}

fn get_last_digit(input: &str) -> String {
    // Find the first digit in the string
    let first_digit = input.chars().rfind(|c| c.is_digit(10));

    // Handle the result
    match first_digit {
        Some(digit) => digit.to_string(),
        None => "".to_string(),
    }
}

fn replace_from_left(line: &str) -> String {
    let mut my_line = String::from(line);
    let replacements = [
        ("one", "o1e"),
        ("two", "t2o"),
        ("three", "t3e"),
        ("four", "f4"),
        ("five", "f5e"),
        ("six", "s6x"),
        ("seven", "s7n"),
        ("eight", "e8t"),
        ("nine", "n9e"),
    ];
    for (old_str, new_str) in &replacements {
        my_line = my_line.replace(old_str, new_str);
    }
    return my_line
}

fn main() {
    let input_path: &str = "./input.txt";
    // let input_path2: &str = "./input2.txt";
    let input_path2: &str = "./puzzle_input.txt";
    let file_content = fs::read_to_string(input_path)
        .expect("Should have been able to read the file");
    let file_content2 = fs::read_to_string(input_path2)
        .expect("Should have been able to read the file");
    let lines = file_content.lines();
    let mut sum: i32 = 0;
    for line in lines {
        let first_digit = get_first_digit(line);
        let last_digit = get_last_digit(line);
        let digit: i32 = format!("{}{}", first_digit, last_digit).parse().unwrap();
        sum += digit;
    }
    println!("Part 1 answer: {}", sum);

    let mut sum2: i32 = 0;
    let lines2 = file_content2.lines();
    for line in lines2 {
        let tmp_line_left = replace_from_left(line);
        let first_digit2 = get_first_digit(&tmp_line_left);
        let last_digit2 = get_last_digit(&tmp_line_left);
        let digit2: i32 = format!("{}{}", first_digit2, last_digit2).parse().unwrap();
        sum2 += digit2;
    }
    println!("Part 2 answer: {}", sum2);
}