import numpy as np 

def function(x):

	v1 = x
	r3 = 9
	paths = []
	try:
		if x <= 9:
			x = v1*x
			paths.append(1)
		else:
			x = 9+x
			paths.append(2)
		if r3 < 8:
			v1 = 0-5
			paths.append(3)
		else:
			x = 7*7
			x = x-r3
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		x = v1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))