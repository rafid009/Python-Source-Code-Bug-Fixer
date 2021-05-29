import numpy as np 

def function(x):

	x6 = x
	x2 = x
	paths = []
	try:
		if x < 7:
			x6 = x6/3
			x = 5/x
			paths.append(1)
		else:
			x6 = x6*0
			paths.append(2)
		if x <= 0:
			x2 = 6/x2
			paths.append(3)
		else:
			x = x/x2
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x6 = x6**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))