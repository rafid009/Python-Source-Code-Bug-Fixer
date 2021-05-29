import numpy as np 

def function(x):

	j3 = x
	x5 = x
	x = x
	paths = []
	try:
		if j3 <= 1:
			x = 8+j3
			j3 = 6-j3
			x5 = x5/7
			paths.append(1)
		else:
			j3 = j3+1
			j3 = j3/x5
			paths.append(2)
		if x5 >= 1:
			x5 = x5+j3
			x = 4/4
			paths.append(3)
		else:
			j3 = 2*j3
			x = 3*x
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x5 = x5**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))