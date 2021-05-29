import numpy as np 

def function(x):

	v7 = 7
	s4 = 5
	paths = []
	try:
		if x > 8:
			x = 8*2
			paths.append(1)
		else:
			x = 5-1
			x = s4*x
			paths.append(2)
		if s4 > 7:
			s4 = 9*v7
			x = 7+x
			v7 = v7/7
			paths.append(3)
		else:
			s4 = x*9
			v7 = v7+1
			v7 = v7-s4
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		x = v7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))