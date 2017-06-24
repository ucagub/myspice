import my_spice as ms

#component_list = ms.read_netlist("test_spice.txt")
component_list = ms.read_netlist("simple.txt")

for component in component_list:
    print(component.getType())
    print(component.getNodes())
    print(component.getName())
    print(component.getModel())
    print("\n")