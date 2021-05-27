import numpy as np 

def function(x):

	a6 = x
	h1 = x
	x = 7
	paths = []
	try:
		if x > 3:
			x = x/8
			a6 = 8-8
			paths.append(1)
		else:
			a6 = 8-a6
			a6 = 6/a6
			paths.append(2)
		if x <= 7:
			x = x*4
			a6 = x*2
			a6 = h1+a6
			paths.append(3)
		else:
			x = x-a6
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		x = h1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))