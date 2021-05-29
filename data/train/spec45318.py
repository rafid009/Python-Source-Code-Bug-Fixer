import numpy as np 

def function(x):

	m1 = 0
	u4 = 8
	paths = []
	try:
		if x < 9:
			m1 = m1-x
			x = u4/1
			paths.append(1)
		else:
			u4 = 0*x
			paths.append(2)
		if m1 <= 8:
			m1 = m1/7
			paths.append(3)
		else:
			x = x+5
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