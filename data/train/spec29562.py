import numpy as np 

def function(x):

	v3 = 9
	g1 = 1
	paths = []
	try:
		if g1 <= 0:
			v3 = v3/v3
			paths.append(1)
		else:
			v3 = x-0
			v3 = g1/v3
			g1 = 7+v3
			paths.append(2)
		if x <= 0:
			x = x-5
			g1 = 3/g1
			paths.append(3)
		else:
			x = x*1
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		v3 = v3**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))