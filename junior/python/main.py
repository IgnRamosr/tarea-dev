from typing import List, Tuple, Dict
import json


def calculate_panels(panel_width: int, panel_height: int, roof_width: int, roof_height: int) -> int:


##### Primero sacamos la cantidad de paneles que caben tanto verticalmente como horizontalmente
    cty_normal_width_panels = roof_width // panel_width
    cty_normal_height_panels = roof_height // panel_height
    total = cty_normal_height_panels * cty_normal_width_panels

### Continuamos sacando el ESPACIO utilizado en la altura y anchura

    used_height_space = cty_normal_height_panels * panel_height
    used_width_space = cty_normal_width_panels * panel_width

### Después necesitamos sacar lo SOBRANTE de la altura

    remaining_height_roof = roof_height - used_height_space

### Por último evaluamos si el sobrante de altura es mayor o igual al ancho del panel 
### con el fin de evaluar si se puede colocar un panel rotado
    if remaining_height_roof >= panel_width:

        rotated_height_panels = roof_width // panel_height
        rotated_width_panels = remaining_height_roof // panel_width

        total += rotated_height_panels * rotated_width_panels


    
    return total


def run_tests() -> None:
    with open('test_cases.json', 'r') as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"]
            }
            for test in data["testCases"]
        ]
    
    print("Corriendo tests:")
    print("-------------------")
    
    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"], test["panel_h"], 
            test["roof_w"], test["roof_h"]
        )
        passed = result == test["expected"]
        
        print(f"Test {i}:")
        print(f"  Panels: {test['panel_w']}x{test['panel_h']}, "
              f"Roof: {test['roof_w']}x{test['roof_h']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    
    run_tests()


if __name__ == "__main__":
    main()
