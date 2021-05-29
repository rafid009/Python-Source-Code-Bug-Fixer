import numpy as np 

def function(x):

	j3 = x
	a8 = 6
	paths = []
	try:
		if a8 <= 5:
			x = a8+x
			x = 2+x
			x = x+x
			paths.append(1)
		else:
			j3 = 1+j3
			a8 = a8/6
			a8 = a8-0
			paths.append(2)
		if a8 > 5:
			j3 = j3/7
			j3 = 3+j3
			paths.append(3)
		else:
			a8 = 1-a8
			j3 = a8/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a8 = x**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))