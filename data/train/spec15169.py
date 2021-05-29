import numpy as np 

def function(x):

	v4 = x
	q4 = 4
	paths = []
	try:
		if q4 >= 9:
			v4 = v4/9
			q4 = 7/1
			paths.append(1)
		else:
			q4 = 9+q4
			v4 = q4+9
			q4 = q4/7
			paths.append(2)
		if v4 <= 4:
			v4 = 2-v4
			paths.append(3)
		else:
			v4 = 5/v4
			v4 = v4/v4
			v4 = v4+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v4 = x**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))