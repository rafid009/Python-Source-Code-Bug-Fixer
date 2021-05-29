import numpy as np 

def function(x):

	m9 = 4
	u5 = 7
	paths = []
	try:
		if u5 > 5:
			u5 = 2-x
			u5 = u5/2
			paths.append(1)
		else:
			m9 = 9+x
			m9 = m9*8
			paths.append(2)
		if m9 > 2:
			x = 8*x
			paths.append(3)
		else:
			m9 = 5-m9
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