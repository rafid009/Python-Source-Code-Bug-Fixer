import numpy as np 

def function(x):

	u6 = x
	j0 = x
	paths = []
	try:
		if u6 < 8:
			j0 = u6+9
			paths.append(1)
		else:
			x = x-3
			u6 = j0-8
			paths.append(2)
		if x >= 5:
			u6 = 2*9
			x = u6*x
			u6 = 0*1
			paths.append(3)
		else:
			x = 4+x
			u6 = x+j0
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		u6 = u6**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))