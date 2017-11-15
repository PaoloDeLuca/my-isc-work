############################
### define function
def double_it(number):
    return 2 * number

#test fun
print double_it(2)
print double_it(2.44)
print double_it('obladioblada') #function also applied to strings

########################
# pitagora's theorem
def calc_hypo(a,b):
    if type(a) not in (int, float) or type(b) not in (int, float):
        print 'error'
        return False
    if a <= 0 or b <= 0:
        print 'error2'
        return False
    hypo = (a**2 + b**2)**(0.5)
    return hypo

print calc_hypo(4,6)
###########


