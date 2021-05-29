import numpy as np 

def function(x):

	v2 = 6
	j6 = 6
	paths = []
	try:
		if x <= 3:
			x = v2+x
			paths.append(1)
		else:
			j6 = 9*j6
			j6 = 3/7
			paths.append(2)
		if v2 <= 5:
			v2 = 2/v2
			paths.append(3)
		else:
			v2 = x*x
			j6 = j6-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v2 = x**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))