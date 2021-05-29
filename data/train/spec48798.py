import numpy as np 

def function(x):

	u9 = x
	s4 = 8
	paths = []
	try:
		if u9 < 6:
			x = x-s4
			s4 = s4/4
			s4 = s4-8
			paths.append(1)
		else:
			x = 0+x
			x = s4+6
			x = x*8
			paths.append(2)
		if x > 9:
			u9 = u9*s4
			u9 = 0/u9
			s4 = s4*0
			paths.append(3)
		else:
			x = x-s4
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		u9 = s4**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))