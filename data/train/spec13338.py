import numpy as np 

def function(x):

	j3 = 3
	v2 = x
	paths = []
	try:
		if j3 < 6:
			v2 = 5/v2
			v2 = v2+2
			v2 = v2+6
			paths.append(1)
		else:
			j3 = 6*5
			v2 = v2/9
			x = x+j3
			paths.append(2)
		if j3 <= 6:
			x = 3-x
			paths.append(3)
		else:
			j3 = j3-8
			v2 = v2/4
			j3 = x+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))