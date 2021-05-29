import numpy as np 

def function(x):

	k7 = 6
	j1 = x
	paths = []
	try:
		if j1 >= 9:
			x = k7+2
			j1 = x+j1
			paths.append(1)
		else:
			x = x/1
			paths.append(2)
		if j1 >= 5:
			x = 3+x
			k7 = k7-1
			paths.append(3)
		else:
			x = x+9
			x = x-k7
			j1 = 9-0
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