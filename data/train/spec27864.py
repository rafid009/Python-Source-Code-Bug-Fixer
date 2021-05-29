import numpy as np 

def function(x):

	e9 = x
	j1 = 5
	paths = []
	try:
		if j1 > 4:
			j1 = e9+j1
			e9 = 4+e9
			paths.append(1)
		else:
			j1 = j1/9
			paths.append(2)
		if j1 < 0:
			e9 = e9/8
			j1 = 2-j1
			e9 = e9/e9
			paths.append(3)
		else:
			j1 = 4*j1
			x = x/4
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		x = e9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))