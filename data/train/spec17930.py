import numpy as np 

def function(x):

	u6 = 4
	n6 = 5
	paths = []
	try:
		if n6 < 9:
			u6 = x-u6
			n6 = 2+n6
			x = x*x
			paths.append(1)
		else:
			u6 = u6+0
			n6 = u6-7
			n6 = n6/4
			paths.append(2)
		if u6 <= 9:
			x = x*5
			x = x/x
			paths.append(3)
		else:
			n6 = n6*8
			n6 = 5/n6
			u6 = u6*x
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