import numpy as np 

def function(x):

	a2 = 0
	i7 = 8
	paths = []
	try:
		if i7 <= 6:
			a2 = a2+0
			x = x/6
			paths.append(1)
		else:
			a2 = a2-i7
			paths.append(2)
		if i7 <= 3:
			i7 = 0/5
			a2 = 6/a2
			x = x+a2
			paths.append(3)
		else:
			x = 1-4
			i7 = 3*i7
			x = i7/a2
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