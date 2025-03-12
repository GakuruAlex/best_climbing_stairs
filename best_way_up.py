from typing import List, Dict
def best_way_up_recur(stairs: int, steps: List[int]) -> List[int]:
    """_Find the shortest combinations of steps up the stairs_

    Args:
        stairs (int): _Number of stairs_
        steps (List[int]): _Number of stairs you are allowed to climb at a time_

    Returns:
        List[int]: _List of shortest way up_
    """
    best_way: List[int] = []
    if stairs == 0:
        return []
    elif stairs < 0:
        return None
    else:
        for step in steps:
            new_stairs: int = stairs - step
            result: List[int] = best_way_up_recur(stairs= new_stairs, steps= steps)
            if result != None:
                current = [step] + result
                if len(current) < len(best_way) or len(best_way) == 0:
                    best_way = current
    return best_way
def best_way_up_memo(stairs: int, steps: List[int] = [2, 1], memo: Dict[int, List[int]] ={0: [], 1: [1], 2: [2]}) -> List[int]:
    """_Find the best way up_

    Args:
        stairs (int): _Number of stairs_
        steps (List[int], optional): _Steps allowed to take at a time_. Defaults to [2, 1].
        memo (_type_, optional): _Dictionary of already calculated sub-problem_. Defaults to {0: [], 1: [1], 2: [2]}.

    Returns:
        List[int]: _description_
    """
    if stairs in memo:
        return memo[stairs]
    if stairs < 0:
        return None
    for step in  steps:
        new_stairs: int = stairs - step
        result: List[int] = best_way_up_memo(stairs= new_stairs, steps= steps, memo=memo)
        if result != None:
            current = [step] + result
        if not stairs in memo or len(current) < len(memo[stairs]) :
                memo[stairs] = current
    return memo[stairs]

def main()-> None:
    steps: List[int] = [2, 1, 3, 5]
    stairs: int = 5
    best_way: List[int] = best_way_up_memo(stairs=stairs, steps= steps)
    print(f"The best way up {stairs} stairs restricted to  one of {steps} steps at a time is {best_way} ")

if __name__ == "__main__":
    main()