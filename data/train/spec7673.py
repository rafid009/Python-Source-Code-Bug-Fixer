import numpy as np 

def function(x):

	e6 = 8
	v3 = x
	paths = []
	try:
		if v3 <= 5:
			v3 = v3*4
			e6 = v3/v3
			paths.append(1)
		else:
			v3 = 2*3
			e6 = e6*6
			paths.append(2)
		if x > 5:
			x = 0-x
			x = x-4
			v3 = v3+x
			paths.append(3)
		else:
			e6 = 0+5
			e6 = 0/v3
			v3 = 9*2
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		x = v3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))