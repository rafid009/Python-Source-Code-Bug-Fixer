import numpy as np 

def function(x):

	m5 = 6
	k6 = 6
	paths = []
	try:
		if x >= 8:
			x = x+7
			k6 = k6/m5
			paths.append(1)
		else:
			m5 = x*m5
			m5 = m5+m5
			paths.append(2)
		if x < 0:
			x = x/4
			paths.append(3)
		else:
			x = 6*x
			x = 9-x
			x = x+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))