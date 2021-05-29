import numpy as np 

def function(x):

	m5 = 4
	i0 = x
	paths = []
	try:
		if i0 <= 4:
			m5 = m5/2
			i0 = x/x
			paths.append(1)
		else:
			x = x+9
			paths.append(2)
		if x > 0:
			x = x*x
			paths.append(3)
		else:
			m5 = m5+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i0 = x**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))