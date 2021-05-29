import numpy as np 

def function(x):

	m6 = 7
	u3 = x
	paths = []
	try:
		if x <= 2:
			m6 = 5*m6
			x = x/2
			paths.append(1)
		else:
			m6 = m6-7
			x = x+9
			x = m6/x
			paths.append(2)
		if m6 <= 6:
			m6 = 8*m6
			paths.append(3)
		else:
			m6 = 8+2
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		x = u3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))