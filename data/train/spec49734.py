import numpy as np 

def function(x):

	l0 = x
	j7 = x
	paths = []
	try:
		if l0 > 9:
			x = 9*x
			l0 = l0*3
			paths.append(1)
		else:
			x = x-2
			j7 = j7-5
			paths.append(2)
		if x < 6:
			l0 = l0-j7
			j7 = j7+1
			paths.append(3)
		else:
			l0 = 7/8
			x = x*8
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