import numpy as np 

def function(x):

	e5 = x
	a2 = x
	paths = []
	try:
		if e5 >= 8:
			e5 = e5/8
			paths.append(1)
		else:
			a2 = a2+a2
			a2 = a2*e5
			paths.append(2)
		if e5 <= 4:
			x = x*8
			a2 = 9/x
			paths.append(3)
		else:
			a2 = a2/6
			x = 1*x
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		x = e5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))