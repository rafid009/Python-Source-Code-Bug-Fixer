import numpy as np 

def function(x):

	i5 = x
	j1 = 9
	paths = []
	try:
		if x < 6:
			j1 = j1-5
			paths.append(1)
		else:
			j1 = 7-j1
			x = x-7
			paths.append(2)
		if i5 <= 3:
			j1 = j1+0
			x = x+3
			paths.append(3)
		else:
			j1 = j1/3
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