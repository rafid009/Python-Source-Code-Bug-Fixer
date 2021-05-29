import numpy as np 

def function(x):

	m3 = x
	o0 = 4
	paths = []
	try:
		if x >= 6:
			x = m3-6
			x = x*1
			o0 = 6*o0
			paths.append(1)
		else:
			x = x*2
			o0 = o0*7
			o0 = 0*7
			paths.append(2)
		if o0 < 2:
			m3 = m3/2
			paths.append(3)
		else:
			m3 = m3-o0
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