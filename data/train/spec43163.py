import numpy as np 

def function(x):

	a2 = x
	a4 = x
	paths = []
	try:
		if a2 > 8:
			a4 = x*a4
			x = a4+x
			a2 = 3/4
			paths.append(1)
		else:
			a2 = a4/a2
			a2 = 3*a4
			a2 = a2-0
			paths.append(2)
		if x < 6:
			a4 = 7+a2
			a2 = a2-a2
			x = a4/x
			paths.append(3)
		else:
			a2 = a2/a4
			a4 = a4+8
			x = x+2
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		a4 = a4**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))