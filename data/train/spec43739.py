import numpy as np 

def function(x):

	u1 = 3
	m8 = x
	paths = []
	try:
		if x >= 7:
			u1 = u1*0
			paths.append(1)
		else:
			m8 = m8+5
			paths.append(2)
		if u1 >= 2:
			x = 2-x
			u1 = m8+u1
			m8 = 2-1
			paths.append(3)
		else:
			m8 = 3+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))