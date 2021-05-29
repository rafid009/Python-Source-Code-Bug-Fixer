import numpy as np 

def function(x):

	m5 = 9
	a4 = 4
	paths = []
	try:
		if m5 > 1:
			x = x*9
			m5 = m5-x
			m5 = x+m5
			paths.append(1)
		else:
			x = m5*x
			x = x/a4
			paths.append(2)
		if a4 > 5:
			x = x+7
			a4 = a4-a4
			a4 = a4+a4
			paths.append(3)
		else:
			a4 = a4-7
			m5 = 8+m5
			m5 = 2-a4
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