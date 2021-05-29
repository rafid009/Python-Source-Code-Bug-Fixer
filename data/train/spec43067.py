import numpy as np 

def function(x):

	n8 = x
	u6 = 3
	x = x
	paths = []
	try:
		if x < 2:
			x = 3-4
			paths.append(1)
		else:
			n8 = n8/2
			n8 = x+1
			x = x/n8
			paths.append(2)
		if u6 < 8:
			n8 = n8+1
			u6 = n8/u6
			paths.append(3)
		else:
			n8 = 0+5
			u6 = 9-4
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		n8 = u6**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))