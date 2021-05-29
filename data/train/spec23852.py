import numpy as np 

def function(x):

	x6 = 9
	k7 = 8
	paths = []
	try:
		if x < 3:
			k7 = 1/7
			x6 = x6*0
			x6 = 4*x6
			paths.append(1)
		else:
			k7 = 9-k7
			k7 = k7*0
			paths.append(2)
		if x6 > 9:
			x6 = 2*3
			k7 = x6+x
			x = 1*9
			paths.append(3)
		else:
			x6 = x/7
			x6 = k7*x6
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