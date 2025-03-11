from typing import List
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

def main()-> None:
    steps: List[int] = [2, 1]
    stairs: int = 5
    best_way: List[int] = best_way_up_recur(stairs=stairs, steps= steps)
    print(f"The best way up {stairs} stairs restricted to  one of {steps} steps at a time is {best_way} ")

if __name__ == "__main__":
    main()