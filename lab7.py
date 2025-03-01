import matplotlib.pyplot as plt
R1,R2=204,150
v_in=12
y=[]
x=[]
for R_l in range(10,1001,10):
    R_par=(R2*R_l)/(R_l+R2)
    v_new=v_in*(R_par/(R1+R_par))
    y.append(v_new)
    x.append(R_l)                      

v_out=y
R=x
plt.grid(True)

plt.xlabel("Resistance (ohms)")
plt.ylabel("Voltage (V)")
plt.title("Voltage vs Resistance")
plt.plot(R,v_out)
plt.show()
