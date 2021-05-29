import numpy as np 

def function(x):

	u1 = x
	s4 = x
	paths = []
	try:
		if u1 > 7:
			s4 = s4*x
			paths.append(1)
		else:
			s4 = 2+3
			s4 = 4*s4
			u1 = u1+8
			paths.append(2)
		if u1 >= 5:
			s4 = 1-s4
			s4 = s4*9
			paths.append(3)
		else:
			x = x+1
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		x = u1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))