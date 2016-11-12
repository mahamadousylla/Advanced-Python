from goody import irange, type_as_str
from calendar import month

class Date:
    month_dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        
        assert type(self.month) == int and type(self.year) == int and type(self.day) == int, 'Typer Error, ' + str(self.month) + ' and ' + str(self.year) + ' and ' + str(self.day) + ' must all be integers'
        assert self.year >= 0 and self.month in range(1, 13), str(self.year) + ' must be greater than 0'
        assert self.days_in(self.year, self.month) >= self.day, str(self.month) + ' does not have ' + str(self.day) + ' days'


    def __getitem__(self, *args):
        alist = [ ]
        for arg in args:
            if arg == 'y':
                return self.year
            elif arg == 'm':
                return self.month
            elif arg == 'd':
                return self.day
            elif type(arg) == tuple:
                for arg in args:
                    for the_arg in arg:
                        if the_arg == 'y':
                            alist.append(self.year)
                        elif the_arg == 'm':
                            alist.append(self.month)
                        elif the_arg == 'd':
                            alist.append(self.day)
            else:
                raise IndexError
        return tuple(alist)
            
    def __str__(self):
        astring = str(self.month) + '/' + str(self.day) + '/' + str(self.year)
        return astring
    
    def __repr__(self):
        astring = 'Date(' + str(self.year) + ',' + str(self.month) + ',' + str(self.day) + ')'
        return astring
        
    
    def __len__(self):

        days = 0
        for year in range(self.year):
            days += 366 if self.is_leap_year(year) else 365
        for month in range(1, self.month):
            days += self.days_in(self.year, month)
        days += self.day - 1
        return days
#         for year in range(0, self.year):
#                      
#             for current_month in range(1, 13):
#                 days += self.days_in(year,current_month)
#               
#         for current_month in range(1, self.month):
#             days += self.days_in(self.year, current_month)
#         days += self.day
#         return days - 1

        
    def __eq__(self, right):
        if type(self) != type(right):
            return False
        
        elif self.year == right.year and self.month == right.month and self.day == right.day:
            return True
        
        else:
            return False
        
    def __lt__(self, right):
        if type(right) != int and type(right) != type(self):
            raise TypeError
        
        if type(self) == type(right):
            return self.__len__() < right.__len__()
        
        elif type(right) == int:
            return self.__len__() < right
    
    def __add__(self, right):
        if type(right) is not int:
            raise TypeError(' unsupported operand type(s) for +: '+type_as_str(self)+' and '+type_as_str(right))
        year,month,day = self['y','m','d']
        for _i in range(abs(right)):
            if right >= 0:
                day += 1
                if day == self.days_in(year,month)+1:
                    day,month = 1, month+1
                    if month == 13:
                        month,year = 1,year+1
            else:
                day -= 1
                if day == 0:
                    month -= 1
                    if month == 0:
                        day,month,year = 31,12,year-1
                    else:
                        day = Date.days_in(year,month)
        return Date(year,month,day)
    
#         if type(right) != int:
#             raise TypeError
#         
#         if right > 0:
#             while right != 0:
#                 
#                 self.day = self.day + 1
#                 if self.days_in(self.year, self.month) == self.day:
#                     self.month += 1
#                     self.day = 0
#                 
#                     
#                 elif self.month == 12 and self.day == 31:
#                     self.year += 1
#                     print(self.year)
#                     self.month = 1
#                     self.day = 0
#                     right -= 1
#                 right -= 1

        
        return self.__str__()
    
    
    def __sub__(self, right):
        if type(self) == type(right):
            new_date = self.__len__() - right.__len__()
            return new_date
        
                
        if type(right) == int:
            new_date = self +  -right
            return new_date
        

    
    def __call__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        
        assert type(self.month) == int and type(self.year) == int and type(self.day) == int, 'Typer Error, ' + str(self.month) + ' and ' + str(self.year) + ' and ' + str(self.day) + ' must all be integers'
        assert self.year >= 0 and self.month in range(1, 13), str(self.year) + ' must be greater than 0'
        assert self.days_in(self.year, self.month) >= self.day, str(self.month) + ' does not have ' + str(self.day) + ' days'        
        
    
    
    
    @staticmethod
    def is_leap_year(year):
        return (year%4 == 0 and year%100 != 0) or year%400 == 0
    
    @staticmethod
    def days_in(year,month):
        return Date.month_dict[month] + (1 if month == 2 and Date.is_leap_year(year) else 0)




    
if __name__ == '__main__':
    # Put in simple tests for Date before allowing driver to run
#     a = Date(16, 4, 21)
#     print(a + 1000)
    print()
    import driver
    
    driver.default_file_name = 'bsc1.txt'
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()



        
        
        
        
        
