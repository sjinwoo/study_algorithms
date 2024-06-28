def validate_range(coord):
    return (-1000 <= coord[0] <= 1000) and (-1000 <= coord[1] <= 1000)

def calc_energy(elements):
    global DIR
    
    result = 0
    
    # 1개만 남을 때 까지 반복
    while len(elements) > 1:
        curr_element_location = {}
        
        for _element in elements:
            _element[0] = _element[0] + DIR[_element[2]][0]     # X
            _element[1] = _element[1] + DIR[_element[2]][1]     # Y
            
            _element_coord = (_element[0], _element[1])
            if _element_coord not in curr_element_location.keys():
                curr_element_location[(_element[0], _element[1])] = [_element]
            else:
                curr_element_location[(_element[0], _element[1])].append(_element)
            
        elements = []
        for _coord, _elements in curr_element_location.items():
            if len(_elements) > 1:
                for _element in _elements:
                    result += _element[-1]
            
            else:
                if validate_range(_coord):
                    elements.extend(_elements)
                        
    return result

if __name__ == "__main__":
    #         상       하       좌      우
    DIR = [(0, 0.5), (0, -0.5), (-0.5, 0), (0.5, 0)]
    T = int(input())

    result_list = []
    
    for idx in range(1, T+1):
        N = int(input())
        elements = [list(map(int, input().split())) for _ in range(N)]

        result = calc_energy(elements)
        result_list.append(result)

    for idx, res in enumerate(result_list, start=1):
        print(f"#{idx} {res}")