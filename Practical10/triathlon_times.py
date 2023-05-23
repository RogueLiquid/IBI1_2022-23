#create a new class "triathlon", containing:
#first and last name, the location, the time for each of the three disciplines, the	person’s total time	over the triathlon
class triathlon:
    def __init__ (self, first_name, last_name, location, time_swim, time_cycle, time_run, total_time):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.time_cycle = str(time_cycle)
        self.time_swim = str(time_swim)
        self.time_run = str(time_run)
        self.total_time = str(total_time)
    def information(self):
        out_put = "first name is "+self.first_name+ "; last_name is "+ self.last_name+ "; location is "+ self.location+ "; swim time is "+ self.time_swim+ "; cycle time is "+ self.time_cycle+ "; run time is "+ self.time_run+ "; total time is "+ self.total_time+"."
        return out_put
athlete1 = triathlon("Homer", "Simpson", "Sprintfield", 100, 30, 200, 330)
athlete2 = triathlon("Marge", "Simpson", "Sprintfield", 50, 15, 100, 165)
print(triathlon.information(athlete1))
print(triathlon.information(athlete2))
