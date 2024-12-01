let rec read file =
    try 
        let line = input_line file in
        line :: (read file)
    with End_of_file -> []

let rec lines_to_lists lines l r =
    match lines with
    | [] -> (List.rev l, List.rev r)
    | line :: rest ->
        let (a, b) = Scanf.sscanf line "%d %d" (fun a b -> (a, b)) in
        lines_to_lists rest (a :: l) (b :: r)

let rec counter l r =
    match l with
    | [] -> 0
    | h :: t -> if h = r then 1 + counter t r else counter t r

let rec part2 a b =
  match a with
  | [] -> 0
  | h :: t -> h*(counter b h) + part2 t b

let () =
    let lines = read stdin in
    let (a, b) = lines_to_lists lines [] [] in
    Printf.printf "%d\n" (part2 a b)