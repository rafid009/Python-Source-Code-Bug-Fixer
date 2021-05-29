import numpy as np 

def function(x):

	s4 = x
	u5 = 1
	paths = []
	try:
		if x > 8:
			u5 = s4+u5
			u5 = 1/7
			paths.append(1)
		else:
			u5 = x+u5
			x = x*5
			u5 = u5-u5
			paths.append(2)
		if s4 < 8:
			u5 = 2+u5
			s4 = s4*0
			s4 = s4-9
			paths.append(3)
		else:
			x = 5*2
			x = 4+7
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		s4 = s4**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))