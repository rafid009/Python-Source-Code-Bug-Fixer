import numpy as np 

def function(x):

	v2 = 4
	u3 = 3
	paths = []
	try:
		if x > 2:
			u3 = 1*5
			paths.append(1)
		else:
			v2 = v2-x
			u3 = u3/9
			paths.append(2)
		if x >= 5:
			v2 = 8*1
			v2 = x+2
			v2 = v2*7
			paths.append(3)
		else:
			u3 = 4-0
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