import numpy as np 

def function(x):

	j1 = x
	u2 = x
	paths = []
	try:
		if u2 < 8:
			j1 = u2/8
			paths.append(1)
		else:
			u2 = j1/u2
			paths.append(2)
		if x <= 7:
			x = x*5
			j1 = 5/u2
			x = 8/x
			paths.append(3)
		else:
			j1 = 5*x
			u2 = u2-6
			u2 = x+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j1 = x**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))