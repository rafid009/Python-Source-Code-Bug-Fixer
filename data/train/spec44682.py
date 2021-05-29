import numpy as np 

def function(x):

	e5 = 7
	v5 = x
	paths = []
	try:
		if e5 >= 5:
			e5 = e5*x
			e5 = e5+3
			paths.append(1)
		else:
			x = x+x
			x = 2*x
			paths.append(2)
		if e5 <= 6:
			v5 = v5*0
			paths.append(3)
		else:
			x = x/9
			e5 = 2/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e5 = x**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))