import numpy as np 

def function(x):

	v4 = x
	a7 = x
	paths = []
	try:
		if x <= 7:
			v4 = a7-6
			paths.append(1)
		else:
			x = 2*x
			x = 5-4
			a7 = 2-7
			paths.append(2)
		if v4 > 2:
			x = v4-4
			paths.append(3)
		else:
			x = x*2
			x = 6/x
			x = x+2
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		a7 = a7**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))