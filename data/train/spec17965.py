import numpy as np 

def function(x):

	m7 = 2
	u8 = 0
	x = 9
	paths = []
	try:
		if x < 4:
			u8 = u8/2
			m7 = m7/m7
			u8 = 8-x
			paths.append(1)
		else:
			u8 = u8-x
			x = x*m7
			m7 = m7-7
			paths.append(2)
		if x >= 1:
			x = x-m7
			paths.append(3)
		else:
			x = u8+x
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		x = u8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))