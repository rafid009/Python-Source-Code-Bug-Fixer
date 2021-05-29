import numpy as np 

def function(x):

	m4 = 6
	u6 = 7
	paths = []
	try:
		if m4 >= 3:
			u6 = 8-u6
			x = x*x
			paths.append(1)
		else:
			u6 = u6*2
			x = u6-u6
			paths.append(2)
		if x > 8:
			m4 = 5-m4
			u6 = 1/u6
			paths.append(3)
		else:
			u6 = 4-u6
			u6 = u6-7
			m4 = 2/6
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