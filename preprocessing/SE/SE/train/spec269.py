import numpy as np 

def function(x):

	u1 = 5
	m0 = x
	paths = []
	try:
		if x <= 8:
			m0 = u1+m0
			u1 = u1/6
			paths.append(1)
		else:
			m0 = 4-m0
			u1 = m0/u1
			paths.append(2)
		if x > 2:
			x = 0/x
			u1 = 0-6
			x = u1-1
			paths.append(3)
		else:
			x = x*u1
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		u1 = u1**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))