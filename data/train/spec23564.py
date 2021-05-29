import numpy as np 

def function(x):

	e6 = x
	a3 = 7
	paths = []
	try:
		if x > 5:
			e6 = x*3
			x = x+x
			e6 = 9+2
			paths.append(1)
		else:
			a3 = x*x
			paths.append(2)
		if e6 < 7:
			e6 = e6-2
			a3 = a3+x
			x = x+0
			paths.append(3)
		else:
			a3 = a3*2
			x = 2*x
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		a3 = a3**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))