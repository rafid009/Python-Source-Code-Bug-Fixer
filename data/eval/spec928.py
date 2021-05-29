import numpy as np 

def function(x):

	a2 = 1
	v4 = x
	paths = []
	try:
		if x <= 1:
			x = x/1
			a2 = a2+1
			a2 = a2*3
			paths.append(1)
		else:
			v4 = v4*8
			v4 = a2+1
			paths.append(2)
		if a2 < 6:
			x = x-0
			a2 = a2*4
			x = 8+x
			paths.append(3)
		else:
			a2 = 2+a2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a2 = x**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))