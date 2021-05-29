import numpy as np 

def function(x):

	e3 = 4
	v4 = x
	x = 5
	paths = []
	try:
		if x > 4:
			e3 = 7-x
			e3 = e3-7
			e3 = e3-3
			paths.append(1)
		else:
			v4 = x+e3
			e3 = x-2
			paths.append(2)
		if v4 <= 6:
			e3 = v4/4
			v4 = v4/4
			x = e3-x
			paths.append(3)
		else:
			v4 = 7-v4
			e3 = 1+x
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		v4 = v4**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))