import numpy as np 

def function(x):

	j1 = 6
	i5 = x
	paths = []
	try:
		if j1 <= 8:
			i5 = i5/i5
			x = x/8
			i5 = j1+i5
			paths.append(1)
		else:
			i5 = 7/i5
			x = x*j1
			i5 = 7*j1
			paths.append(2)
		if x <= 8:
			x = x/6
			paths.append(3)
		else:
			j1 = 6/j1
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