import numpy as np 

def function(x):

	l6 = 9
	r1 = 1
	paths = []
	try:
		if r1 >= 9:
			l6 = l6+x
			l6 = 5/x
			x = x*2
			paths.append(1)
		else:
			x = x*r1
			paths.append(2)
		if x > 3:
			l6 = l6+3
			paths.append(3)
		else:
			l6 = l6+0
			x = 9/x
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