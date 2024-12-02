let rec read file =
  try
    let line = input_line file in
    line :: (read file)
  with End_of_file -> []

let rec lines_to_list lines =
  match lines with
  | [] -> []
  | h :: t -> (List.map int_of_string (String.split_on_char ' ' h)) :: (lines_to_list t)

let safe levels =
  let rec safe_positive levels =
    match levels with
    | [] -> true
    | h :: [] -> true
    | f :: s :: t -> 
      if (s-f > 0) && (s-f <= 3) then
        safe_positive (s::t)
      else
        false
  in
  let rec safe_negative levels =
    match levels with
    | [] -> true
    | h :: [] -> true
    | f :: s :: t ->
      if (f-s > 0) && (f-s <= 3) then
        safe_negative (s::t)
      else
        false
  in
  match levels with
  | [] -> true
  | h :: [] -> true
  | f :: s :: t when s-f > 0 -> safe_positive levels
  | f :: s :: t -> safe_negative levels

let rec part1 levels =
  match levels with
  | [] -> 0
  | h :: t -> (if safe h then 1 else 0) + part1 t

let rec part2 levels =
  let rec aux left right =
    match right with
    | [] -> if safe left then 1 else 0
    | h :: t -> 
      if safe (left@t) then
        1
      else
        aux (left@[h]) t
  in
  match levels with
  | [] -> 0
  | h :: t -> aux [] h + part2 t

let () = 
  let lines = read (open_in "2/input.txt") in
  let levels = lines_to_list lines in
  Printf.printf "part1 : %d\n" (part1 levels);
  Printf.printf "part2 : %d\n" (part2 levels)