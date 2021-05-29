import numpy as np 

def function(x):

	q3 = x
	v9 = x
	paths = []
	try:
		if x >= 7:
			x = x*x
			q3 = 2/9
			paths.append(1)
		else:
			v9 = v9+x
			v9 = v9/8
			v9 = v9+v9
			paths.append(2)
		if v9 >= 3:
			v9 = 1-q3
			x = x-1
			paths.append(3)
		else:
			v9 = 9*v9
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		v9 = q3**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))