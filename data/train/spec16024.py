import numpy as np 

def function(x):

	a8 = 2
	v3 = x
	paths = []
	try:
		if x >= 0:
			x = x*8
			paths.append(1)
		else:
			a8 = a8/7
			a8 = x/9
			a8 = 5+v3
			paths.append(2)
		if a8 > 2:
			v3 = v3+6
			v3 = v3+x
			paths.append(3)
		else:
			v3 = x+8
			x = x*6
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		x = a8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))