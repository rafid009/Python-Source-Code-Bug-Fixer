import numpy as np 

def function(x):

	o0 = x
	m5 = 8
	paths = []
	try:
		if x < 0:
			x = 4+x
			m5 = 7/m5
			o0 = o0-4
			paths.append(1)
		else:
			o0 = o0*6
			paths.append(2)
		if o0 < 0:
			o0 = 2-o0
			m5 = 6+m5
			paths.append(3)
		else:
			x = 0/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o0 = x**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))