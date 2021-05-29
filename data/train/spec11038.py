import numpy as np 

def function(x):

	j4 = 3
	b4 = 4
	paths = []
	try:
		if x > 0:
			j4 = j4*j4
			b4 = x+1
			b4 = 0-j4
			paths.append(1)
		else:
			x = x+3
			j4 = 6-j4
			x = 2*x
			paths.append(2)
		if j4 >= 8:
			b4 = 2+b4
			paths.append(3)
		else:
			j4 = 2+j4
			j4 = 2-j4
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		x = j4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))