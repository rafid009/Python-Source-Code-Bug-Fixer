import numpy as np 

def function(x):

	v5 = 1
	a0 = x
	paths = []
	try:
		if x >= 5:
			x = x+v5
			paths.append(1)
		else:
			v5 = 2*v5
			a0 = a0-2
			x = x*1
			paths.append(2)
		if v5 < 9:
			v5 = 1-v5
			paths.append(3)
		else:
			x = x+a0
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		a0 = a0**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))