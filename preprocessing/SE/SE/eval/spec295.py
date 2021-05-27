import numpy as np 

def function(x):

	u3 = x
	j6 = x
	paths = []
	try:
		if x < 2:
			x = x+1
			paths.append(1)
		else:
			u3 = 6-3
			j6 = 5/1
			j6 = 4*j6
			paths.append(2)
		if j6 < 6:
			u3 = u3+u3
			u3 = 9+x
			u3 = 6+u3
			paths.append(3)
		else:
			u3 = u3+2
			x = 8/x
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