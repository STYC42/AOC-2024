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

let rec part1 a b =
    match (a, b) with
    | [], [] -> 0
    | a :: rest_a, b :: rest_b ->
        abs (a - b) + part1 rest_a rest_b
    | _ -> failwith "Invalid input"

let () =
    let lines = read stdin in
    let (a, b) = lines_to_lists lines [] [] in
    let c = List.sort compare a in
    let d = List.sort compare b in
    Printf.printf "%d\n" (part1 c d)



