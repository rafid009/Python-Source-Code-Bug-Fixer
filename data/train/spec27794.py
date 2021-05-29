import numpy as np 

def function(x):

	r3 = 1
	x9 = x
	paths = []
	try:
		if r3 <= 2:
			x = x*7
			x = x-x9
			paths.append(1)
		else:
			r3 = r3+9
			r3 = 0-r3
			r3 = x/9
			paths.append(2)
		if r3 >= 6:
			r3 = x/1
			paths.append(3)
		else:
			x9 = x9*3
			x = x9*x
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x = x9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))