import numpy as np 

def function(x):

	j8 = x
	a0 = x
	paths = []
	try:
		if a0 <= 6:
			a0 = a0-a0
			j8 = x/5
			paths.append(1)
		else:
			a0 = 0*5
			x = 6-x
			paths.append(2)
		if j8 > 3:
			j8 = 2+9
			x = a0-x
			a0 = x*a0
			paths.append(3)
		else:
			x = x+8
			j8 = 1*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a0 = x**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))