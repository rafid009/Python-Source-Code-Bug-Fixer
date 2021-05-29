import numpy as np 

def function(x):

	m9 = 0
	u8 = x
	paths = []
	try:
		if u8 > 2:
			u8 = x/7
			paths.append(1)
		else:
			u8 = 6+x
			u8 = x*2
			x = 2-x
			paths.append(2)
		if x < 3:
			m9 = m9+6
			x = m9*x
			x = x+1
			paths.append(3)
		else:
			m9 = m9-m9
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