import numpy as np 

def function(x):

	k4 = x
	k7 = x
	paths = []
	try:
		if k4 <= 4:
			x = k4/8
			x = 7+x
			x = x+x
			paths.append(1)
		else:
			k7 = 4+k7
			x = x/1
			paths.append(2)
		if k7 >= 9:
			x = x*k4
			paths.append(3)
		else:
			k7 = 8+k7
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		x = k7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))