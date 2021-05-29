import numpy as np 

def function(x):

	u5 = x
	m1 = x
	x = 0
	paths = []
	try:
		if x > 0:
			x = 2-6
			x = m1-7
			paths.append(1)
		else:
			x = 5*u5
			x = x*5
			m1 = m1-x
			paths.append(2)
		if x > 5:
			m1 = 7/m1
			x = 6/x
			paths.append(3)
		else:
			u5 = u5*2
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		x = u5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))