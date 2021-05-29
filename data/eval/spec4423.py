import numpy as np 

def function(x):

	u6 = 1
	n6 = 1
	paths = []
	try:
		if u6 <= 1:
			u6 = u6-x
			paths.append(1)
		else:
			n6 = 0*4
			paths.append(2)
		if x < 5:
			u6 = u6-9
			paths.append(3)
		else:
			u6 = u6-9
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		n6 = u6**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))