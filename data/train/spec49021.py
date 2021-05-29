import numpy as np 

def function(x):

	m1 = 1
	o1 = x
	paths = []
	try:
		if o1 > 0:
			m1 = m1+4
			o1 = o1-m1
			paths.append(1)
		else:
			o1 = o1/x
			m1 = 1*2
			x = x*5
			paths.append(2)
		if o1 > 7:
			x = 7+x
			m1 = m1-1
			paths.append(3)
		else:
			o1 = o1-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m1 = x**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))