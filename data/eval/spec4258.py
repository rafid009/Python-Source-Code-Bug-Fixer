import numpy as np 

def function(x):

	i4 = x
	u6 = 1
	paths = []
	try:
		if i4 > 8:
			x = x+6
			u6 = x/2
			u6 = u6+5
			paths.append(1)
		else:
			x = 6+4
			u6 = u6*1
			x = x+u6
			paths.append(2)
		if u6 >= 5:
			x = x*2
			paths.append(3)
		else:
			x = x*i4
			u6 = u6-8
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