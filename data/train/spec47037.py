import numpy as np 

def function(x):

	m5 = 7
	u2 = 1
	x = x
	paths = []
	try:
		if u2 <= 9:
			u2 = 4/u2
			u2 = 5*7
			u2 = u2/m5
			paths.append(1)
		else:
			u2 = u2+4
			x = u2/x
			x = 5*x
			paths.append(2)
		if m5 <= 8:
			x = x-m5
			m5 = x*x
			x = x*2
			paths.append(3)
		else:
			x = x+6
			u2 = 5*m5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u2 = x**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))