import numpy as np 

def function(x):

	x4 = x
	a6 = x
	paths = []
	try:
		if x4 > 2:
			x4 = x4*x4
			a6 = 1*9
			paths.append(1)
		else:
			x = 0/x
			x4 = 1+x4
			x = x*0
			paths.append(2)
		if x <= 5:
			x4 = 0-x4
			a6 = 4-x
			a6 = 2+2
			paths.append(3)
		else:
			a6 = 9+a6
			a6 = x-6
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		x4 = a6**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))