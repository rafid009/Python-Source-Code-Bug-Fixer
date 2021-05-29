import numpy as np 

def function(x):

	o0 = 9
	m2 = 6
	paths = []
	try:
		if o0 <= 6:
			o0 = o0/9
			o0 = o0/x
			paths.append(1)
		else:
			o0 = 0-o0
			paths.append(2)
		if o0 < 3:
			m2 = 1-8
			paths.append(3)
		else:
			x = 1/m2
			m2 = o0+m2
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		x = m2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))