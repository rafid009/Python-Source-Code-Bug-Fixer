import numpy as np 

def function(x):

	o0 = x
	m1 = 5
	paths = []
	try:
		if o0 < 6:
			m1 = m1-8
			paths.append(1)
		else:
			o0 = o0+x
			x = 3/x
			x = x+2
			paths.append(2)
		if x <= 4:
			m1 = 0/m1
			m1 = m1+2
			x = m1-x
			paths.append(3)
		else:
			o0 = o0+5
			o0 = m1*o0
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