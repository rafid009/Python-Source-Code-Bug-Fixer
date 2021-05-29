import numpy as np 

def function(x):

	x3 = 8
	a9 = x
	paths = []
	try:
		if x3 < 0:
			x3 = x3*4
			x = 4+1
			paths.append(1)
		else:
			x3 = x+3
			paths.append(2)
		if x3 >= 7:
			x = 0+x
			a9 = a9+a9
			a9 = x*2
			paths.append(3)
		else:
			a9 = a9-x3
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		x3 = a9**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))