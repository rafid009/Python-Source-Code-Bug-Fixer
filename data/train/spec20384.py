import numpy as np 

def function(x):

	m6 = 6
	u6 = x
	paths = []
	try:
		if u6 < 7:
			m6 = 8*0
			x = m6-x
			paths.append(1)
		else:
			m6 = m6*m6
			u6 = 2-u6
			paths.append(2)
		if m6 <= 2:
			x = 4-x
			x = x*7
			paths.append(3)
		else:
			x = m6/x
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		x = u6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))