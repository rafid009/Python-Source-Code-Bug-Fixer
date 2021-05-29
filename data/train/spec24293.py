import numpy as np 

def function(x):

	u6 = 6
	n2 = 3
	paths = []
	try:
		if u6 < 4:
			u6 = u6+7
			n2 = n2+n2
			paths.append(1)
		else:
			n2 = n2/7
			n2 = 3-6
			u6 = u6/5
			paths.append(2)
		if n2 <= 0:
			u6 = u6/4
			u6 = 7+x
			u6 = 9*u6
			paths.append(3)
		else:
			x = x+7
			x = 9-2
			x = x*6
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