import numpy as np 

def function(x):

	u2 = 0
	l3 = x
	paths = []
	try:
		if u2 < 2:
			l3 = l3-9
			l3 = 3-u2
			l3 = l3+4
			paths.append(1)
		else:
			x = x*x
			l3 = 4-l3
			paths.append(2)
		if l3 >= 7:
			x = x/1
			paths.append(3)
		else:
			u2 = x+l3
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