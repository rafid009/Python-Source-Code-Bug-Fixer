import numpy as np 

def function(x):

	e0 = 9
	i4 = x
	paths = []
	try:
		if e0 > 4:
			i4 = e0+i4
			e0 = e0*2
			e0 = e0*7
			paths.append(1)
		else:
			e0 = x*e0
			paths.append(2)
		if e0 >= 0:
			i4 = 7+4
			paths.append(3)
		else:
			x = x/x
			e0 = i4*i4
			x = 3*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i4 = x**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))