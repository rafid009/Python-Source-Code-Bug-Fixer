import numpy as np 

def function(x):

	u7 = x
	m1 = 4
	paths = []
	try:
		if x < 8:
			x = x+9
			m1 = m1*m1
			m1 = 6*8
			paths.append(1)
		else:
			u7 = m1/m1
			x = 2*x
			u7 = x*5
			paths.append(2)
		if m1 >= 6:
			m1 = 5+m1
			m1 = m1+6
			x = x/x
			paths.append(3)
		else:
			u7 = 4*m1
			u7 = u7*7
			u7 = u7+2
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		x = u7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))