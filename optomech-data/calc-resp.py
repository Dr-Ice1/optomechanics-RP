dV132_1 = 8*(.84-.33)
p132_1 = 17.5
dV132_2 = 8*(.84-.3297)
p132_2 = 18
dV132_3 = 8*(.856-.349)
p132_3 = 18

l = 635e-9

p5_1 = 6
dV5_1 = 3*(.8522-.4267)
p5_2 = 6
dV5_2 = 3*(.866-.44)
p5_3 = 6
dV5_3 = 3*(.895-.454)


def resp(p, dV):
    return p*l/2/dV

r132 = [resp(p132_1, dV132_1), resp(p132_2, dV132_2), resp(p132_3, dV132_3)]
r5 = [resp(p5_1, dV5_1), resp(p5_2, dV5_2), resp(p5_3,dV5_3)]

rounded132 = [f"{n:.3e}" for n in r132]
rounded5 = [f"{n:.3e}" for n in r5]

print(f'Responsivity for 13.2 Vpp is {rounded132} m/V')
print(f'Responsivity for 5.00 Vpp is {rounded5} m/V')
