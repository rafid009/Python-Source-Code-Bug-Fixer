import numpy as np 

def function(x):

	a2 = 5
	i5 = x
	paths = []
	try:
		if i5 < 1:
			x = 4/8
			x = x-a2
			a2 = 7+i5
			paths.append(1)
		else:
			x = a2-6
			i5 = i5/2
			paths.append(2)
		if x > 7:
			i5 = a2*6
			x = 8+6
			paths.append(3)
		else:
			a2 = a2-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a2 = x**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))