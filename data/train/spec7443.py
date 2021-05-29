import numpy as np 

def function(x):

	u8 = x
	m9 = 7
	x = 7
	paths = []
	try:
		if x <= 0:
			u8 = 0-7
			paths.append(1)
		else:
			m9 = 7/m9
			u8 = x-u8
			paths.append(2)
		if u8 <= 6:
			u8 = u8*6
			x = 1*x
			paths.append(3)
		else:
			x = x*x
			m9 = m9*m9
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		u8 = u8**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))