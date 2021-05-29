import numpy as np 

def function(x):

	m5 = 4
	u9 = 7
	paths = []
	try:
		if x > 8:
			x = m5+x
			m5 = 0+m5
			paths.append(1)
		else:
			m5 = 0+m5
			m5 = 3*m5
			paths.append(2)
		if m5 > 0:
			x = x+x
			u9 = x/m5
			paths.append(3)
		else:
			u9 = u9+u9
			m5 = x*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u9 = x**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))