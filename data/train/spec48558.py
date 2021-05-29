import numpy as np 

def function(x):

	e9 = x
	v2 = 9
	paths = []
	try:
		if v2 > 6:
			e9 = x+e9
			e9 = e9+0
			x = 3*0
			paths.append(1)
		else:
			e9 = e9/1
			v2 = 3-5
			paths.append(2)
		if x >= 1:
			x = e9*1
			paths.append(3)
		else:
			x = x-x
			x = 2*x
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		v2 = e9**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))