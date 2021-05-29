import numpy as np 

def function(x):

	o7 = x
	m5 = 9
	paths = []
	try:
		if m5 < 2:
			x = o7/x
			m5 = o7-m5
			paths.append(1)
		else:
			o7 = o7*m5
			m5 = 5+x
			m5 = 4*9
			paths.append(2)
		if m5 > 6:
			m5 = 3/x
			m5 = 4/m5
			paths.append(3)
		else:
			m5 = 1/o7
			m5 = 5*3
			o7 = o7*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o7 = x**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))