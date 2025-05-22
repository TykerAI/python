# In các số chẵn chia hết cho 3 bé hơn 100

for i in range(100):
    if i % 2 == 0:      
        if i % 3 == 0:
            print(f"Các số chẵn chia hết cho 3 bé hơn 100 là: {i}")
