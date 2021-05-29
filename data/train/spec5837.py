import numpy as np 

def function(x):

	v2 = 8
	e7 = x
	paths = []
	try:
		if e7 >= 3:
			v2 = v2/6
			v2 = 2*v2
			paths.append(1)
		else:
			x = e7-x
			x = e7+x
			v2 = x+x
			paths.append(2)
		if v2 >= 4:
			v2 = v2/v2
			v2 = 1+x
			x = x/1
			paths.append(3)
		else:
			x = 7/x
			x = x/1
			e7 = v2-5
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		v2 = e7**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))