class Solution:
   def totalMoney(self,n):
    total = 0        # total money saved
    week_start = 1   # Monday’s amount

    while n > 0:
        # Loop through one week (7 days)
        for day in range(7):
            if n == 0:
                break  # stop when all days counted
            total += week_start + day  # add today's saving
            n -= 1                     # one day completed
        week_start += 1  # next week Monday increases by $1

    return total