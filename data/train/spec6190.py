import numpy as np 

def function(x):

	a1 = 4
	v5 = x
	paths = []
	try:
		if a1 >= 0:
			v5 = v5-0
			paths.append(1)
		else:
			v5 = 0-v5
			paths.append(2)
		if a1 > 4:
			v5 = 0*a1
			a1 = a1/2
			paths.append(3)
		else:
			x = v5-a1
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		x = v5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))