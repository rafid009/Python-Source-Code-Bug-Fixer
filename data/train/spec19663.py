import numpy as np 

def function(x):

	l3 = 8
	s7 = x
	x = 6
	paths = []
	try:
		if x >= 6:
			l3 = s7+s7
			x = x-9
			paths.append(1)
		else:
			x = 5+8
			paths.append(2)
		if s7 < 9:
			x = x*3
			x = x+9
			x = 9*1
			paths.append(3)
		else:
			l3 = 4*l3
			x = x/5
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		x = l3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))