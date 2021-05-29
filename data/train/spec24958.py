import numpy as np 

def function(x):

	a7 = 3
	j9 = x
	paths = []
	try:
		if x < 8:
			x = x-j9
			j9 = 3*j9
			a7 = a7-j9
			paths.append(1)
		else:
			a7 = a7-6
			paths.append(2)
		if x <= 1:
			a7 = x*4
			paths.append(3)
		else:
			x = x+j9
			x = x*4
			x = j9-9
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		j9 = a7**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))