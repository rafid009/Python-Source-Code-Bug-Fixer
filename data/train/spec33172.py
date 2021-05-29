import numpy as np 

def function(x):

	r9 = 0
	a2 = 0
	paths = []
	try:
		if x >= 5:
			r9 = r9*5
			paths.append(1)
		else:
			r9 = r9+9
			a2 = x+8
			paths.append(2)
		if r9 <= 2:
			r9 = a2*2
			paths.append(3)
		else:
			a2 = r9*a2
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		a2 = a2**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))