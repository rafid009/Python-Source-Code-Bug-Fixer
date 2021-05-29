import numpy as np 

def function(x):

	m1 = x
	u5 = x
	x = x
	paths = []
	try:
		if m1 > 6:
			u5 = u5-6
			u5 = 2*1
			paths.append(1)
		else:
			x = 1-u5
			paths.append(2)
		if x < 5:
			m1 = 8*m1
			paths.append(3)
		else:
			x = x*x
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		u5 = m1**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))