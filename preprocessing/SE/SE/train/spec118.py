import numpy as np 

def function(x):

	j4 = x
	u0 = 3
	paths = []
	try:
		if j4 >= 7:
			j4 = 5/2
			u0 = x/u0
			j4 = u0-j4
			paths.append(1)
		else:
			x = x*9
			paths.append(2)
		if u0 >= 7:
			j4 = j4-0
			paths.append(3)
		else:
			j4 = 6-j4
			u0 = 0*0
			j4 = j4+7
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