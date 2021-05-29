import numpy as np 

def function(x):

	u5 = 1
	m6 = 9
	paths = []
	try:
		if x <= 8:
			u5 = 2*u5
			m6 = x+u5
			x = 9*3
			paths.append(1)
		else:
			u5 = m6+1
			m6 = m6/u5
			paths.append(2)
		if x < 4:
			u5 = 6*u5
			x = x*5
			paths.append(3)
		else:
			x = 0+x
			m6 = m6-2
			x = x*m6
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		x = m6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))