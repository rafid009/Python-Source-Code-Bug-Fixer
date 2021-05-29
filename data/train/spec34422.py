import numpy as np 

def function(x):

	m1 = x
	u6 = 2
	x = 9
	paths = []
	try:
		if x < 8:
			u6 = u6/4
			paths.append(1)
		else:
			m1 = m1+4
			u6 = 7+u6
			paths.append(2)
		if u6 >= 2:
			m1 = m1-3
			x = x-m1
			paths.append(3)
		else:
			m1 = 1*5
			m1 = 9-5
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		x = m1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))