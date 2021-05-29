import numpy as np 

def function(x):

	j1 = x
	e2 = x
	paths = []
	try:
		if j1 <= 8:
			e2 = e2*3
			paths.append(1)
		else:
			j1 = 7-5
			paths.append(2)
		if j1 < 5:
			x = 4*x
			paths.append(3)
		else:
			x = x/7
			e2 = 0+e2
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		e2 = j1**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))