import numpy as np 

def function(x):

	j4 = 2
	u4 = 1
	paths = []
	try:
		if u4 >= 7:
			x = 5+j4
			u4 = u4+1
			x = j4*0
			paths.append(1)
		else:
			j4 = j4/6
			u4 = 4+j4
			x = j4-2
			paths.append(2)
		if j4 >= 1:
			x = 9/x
			x = 8*x
			paths.append(3)
		else:
			j4 = 2-j4
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