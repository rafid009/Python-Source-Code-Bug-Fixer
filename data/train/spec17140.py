import numpy as np 

def function(x):

	a7 = 0
	s5 = 2
	paths = []
	try:
		if s5 >= 7:
			x = a7-6
			s5 = 7/4
			s5 = s5*0
			paths.append(1)
		else:
			x = 9/9
			x = x-7
			paths.append(2)
		if x < 3:
			x = s5+x
			paths.append(3)
		else:
			x = 6*8
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