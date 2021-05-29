import numpy as np 

def function(x):

	v3 = 2
	a2 = x
	paths = []
	try:
		if v3 <= 8:
			a2 = a2-a2
			a2 = 0-a2
			v3 = 5+3
			paths.append(1)
		else:
			v3 = 6+9
			x = x*6
			paths.append(2)
		if v3 < 4:
			x = x-x
			paths.append(3)
		else:
			x = x*v3
			a2 = a2+a2
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