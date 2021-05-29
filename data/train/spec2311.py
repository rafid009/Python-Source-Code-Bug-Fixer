import numpy as np 

def function(x):

	u5 = x
	m5 = x
	x = 9
	paths = []
	try:
		if u5 > 5:
			x = x+8
			x = 4+u5
			paths.append(1)
		else:
			u5 = 7-u5
			u5 = m5-u5
			paths.append(2)
		if u5 >= 1:
			x = 7/u5
			u5 = 5/u5
			u5 = m5/1
			paths.append(3)
		else:
			x = x*m5
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		m5 = u5**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))