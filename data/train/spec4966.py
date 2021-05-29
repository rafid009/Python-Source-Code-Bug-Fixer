import numpy as np 

def function(x):

	u2 = 4
	e5 = x
	paths = []
	try:
		if u2 < 8:
			x = x+1
			e5 = e5/3
			paths.append(1)
		else:
			x = x*0
			e5 = e5+3
			u2 = x+x
			paths.append(2)
		if x > 8:
			e5 = e5*6
			paths.append(3)
		else:
			e5 = e5/1
			u2 = 2*0
			e5 = 5/e5
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