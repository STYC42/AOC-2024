let read filename =
  let file = open_in filename in
  let rec read_lines acc =
    try
      let line = input_line file in
      read_lines (line :: acc)
    with End_of_file ->
      close_in file;
      List.rev acc
  in
  String.concat "\n" (read_lines [])

let part1 txt =
  let re = Str.regexp "mul(\\(-?[0-9]+\\),\\s*\\(-?[0-9]+\\))" in
  let rec aux pos acc =
    try
      let pos = Str.search_forward re txt pos in
      let a = int_of_string (Str.matched_group 1 txt) in
      let b = int_of_string (Str.matched_group 2 txt) in
      aux (pos + 1) (acc + a * b)
    with Not_found -> acc
  in
  aux 0 0

let part2 txt =
  let parts = Str.split (Str.regexp "do()") txt in
  let rec aux parts acc =
    match parts with
    | [] -> acc
    | hd :: tl ->
      let s = Str.split (Str.regexp "don't()") hd in
      aux tl (acc + part1 (List.hd s))
  in
  aux parts 0

let () =
  let txt = read "3/input.txt" in
  Printf.printf "Part 1: %d\n" (part1 txt);
  Printf.printf "Part 2: %d\n" (part2 txt)