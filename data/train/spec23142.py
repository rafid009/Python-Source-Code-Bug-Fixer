import numpy as np 

def function(x):

	i0 = x
	j1 = x
	x = 6
	paths = []
	try:
		if i0 > 0:
			j1 = 4*x
			x = 4-x
			paths.append(1)
		else:
			j1 = j1*6
			i0 = x+0
			paths.append(2)
		if j1 <= 3:
			x = 5*1
			j1 = x*j1
			paths.append(3)
		else:
			i0 = j1-i0
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