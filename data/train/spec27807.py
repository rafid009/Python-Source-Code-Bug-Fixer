import numpy as np 

def function(x):

	i0 = 7
	e5 = x
	paths = []
	try:
		if i0 > 9:
			e5 = e5-9
			x = x*4
			e5 = e5+3
			paths.append(1)
		else:
			x = 1*x
			x = e5/e5
			paths.append(2)
		if x <= 1:
			x = x+x
			e5 = e5*7
			paths.append(3)
		else:
			e5 = e5/4
			i0 = 3-4
			x = 9*1
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		e5 = e5**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))