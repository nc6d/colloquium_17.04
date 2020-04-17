"""50. У лотереї розігрувалося 100 квитків. Таблиця містить 10 номерів
виграшних квитків. Перевірте, чи є квиток з номером N виграшним."""
import random
N = int(input("Enter your ticket number: "))
happy_tickets = {random.randint(0, 100) for x in range(11)}
print("Happy tickets:\n", happy_tickets)
if N in happy_tickets:
    print('Congratulations!')
else:
    print('Try next time')
