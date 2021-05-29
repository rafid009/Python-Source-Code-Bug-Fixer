import numpy as np 

def function(x):

	a7 = x
	e0 = 1
	x = 9
	paths = []
	try:
		if x > 1:
			x = e0+2
			x = e0*x
			x = a7+x
			paths.append(1)
		else:
			x = a7-5
			e0 = a7*e0
			paths.append(2)
		if e0 <= 6:
			e0 = a7*4
			paths.append(3)
		else:
			a7 = 4*2
			x = x/3
			a7 = a7-4
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