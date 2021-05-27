import numpy as np 

def function(x):

	a2 = 5
	s7 = x
	paths = []
	try:
		if a2 < 4:
			s7 = x+s7
			paths.append(1)
		else:
			x = 0/x
			a2 = 7*1
			a2 = a2*4
			paths.append(2)
		if x > 2:
			s7 = s7+s7
			s7 = 2/a2
			paths.append(3)
		else:
			a2 = 1+a2
			a2 = a2*9
			a2 = a2-s7
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		x = a2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))