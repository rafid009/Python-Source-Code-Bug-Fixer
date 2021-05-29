import numpy as np 

def function(x):

	u6 = x
	o1 = 8
	paths = []
	try:
		if x >= 6:
			o1 = 8-o1
			u6 = x-x
			o1 = o1+9
			paths.append(1)
		else:
			o1 = o1+x
			paths.append(2)
		if u6 <= 8:
			o1 = u6*4
			x = 4*8
			o1 = 9-o1
			paths.append(3)
		else:
			o1 = o1*u6
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