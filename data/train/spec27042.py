import numpy as np 

def function(x):

	i6 = 2
	u6 = 1
	paths = []
	try:
		if u6 < 0:
			i6 = i6*8
			u6 = u6/6
			paths.append(1)
		else:
			u6 = x+2
			paths.append(2)
		if x > 1:
			x = i6/x
			x = x*3
			x = x+1
			paths.append(3)
		else:
			i6 = 1/u6
			x = x-i6
			x = 3*4
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		x = u6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))