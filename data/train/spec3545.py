import numpy as np 

def function(x):

	s7 = x
	u1 = x
	paths = []
	try:
		if x < 8:
			x = 1-4
			paths.append(1)
		else:
			s7 = 0/s7
			x = s7*0
			u1 = u1-x
			paths.append(2)
		if u1 <= 5:
			s7 = s7/5
			x = s7*4
			u1 = s7*s7
			paths.append(3)
		else:
			x = u1+x
			s7 = 7*s7
			s7 = s7/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))