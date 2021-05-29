import numpy as np 

def function(x):

	u8 = 9
	m1 = x
	paths = []
	try:
		if x >= 5:
			x = x/8
			paths.append(1)
		else:
			u8 = u8/m1
			paths.append(2)
		if m1 < 1:
			m1 = m1+u8
			x = x/7
			paths.append(3)
		else:
			x = 3/x
			x = m1/3
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		u8 = m1**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))