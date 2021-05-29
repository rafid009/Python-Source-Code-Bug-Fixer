import numpy as np 

def function(x):

	v5 = 6
	a8 = 9
	paths = []
	try:
		if x <= 4:
			a8 = 3/v5
			v5 = 3-5
			paths.append(1)
		else:
			x = x*x
			v5 = 9/v5
			x = x+3
			paths.append(2)
		if a8 > 7:
			a8 = 7+a8
			v5 = v5+2
			v5 = v5+9
			paths.append(3)
		else:
			v5 = v5+x
			a8 = a8/4
			v5 = x-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v5 = x**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))