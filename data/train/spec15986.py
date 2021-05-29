import numpy as np 

def function(x):

	h1 = x
	e4 = 0
	paths = []
	try:
		if e4 <= 4:
			e4 = e4/2
			paths.append(1)
		else:
			x = x/h1
			e4 = e4/e4
			paths.append(2)
		if e4 > 8:
			x = x*7
			paths.append(3)
		else:
			e4 = e4/3
			h1 = h1+3
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		x = h1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))