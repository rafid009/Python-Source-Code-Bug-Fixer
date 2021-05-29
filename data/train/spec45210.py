import numpy as np 

def function(x):

	j4 = 9
	f1 = x
	paths = []
	try:
		if x < 1:
			f1 = f1*6
			j4 = j4+0
			paths.append(1)
		else:
			j4 = 0+j4
			paths.append(2)
		if f1 <= 9:
			j4 = f1/f1
			paths.append(3)
		else:
			x = f1+x
			x = j4-x
			j4 = j4+9
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