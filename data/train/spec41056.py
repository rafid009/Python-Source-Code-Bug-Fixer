import numpy as np 

def function(x):

	j9 = x
	a5 = 1
	paths = []
	try:
		if j9 < 5:
			a5 = 4-a5
			paths.append(1)
		else:
			j9 = 4+j9
			j9 = a5/8
			j9 = a5*8
			paths.append(2)
		if a5 < 1:
			j9 = j9-8
			x = x+j9
			a5 = 7+a5
			paths.append(3)
		else:
			a5 = 3*8
			a5 = 0/1
			j9 = j9+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j9 = x**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))