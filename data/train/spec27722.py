import numpy as np 

def function(x):

	o5 = 3
	m6 = x
	x = 3
	paths = []
	try:
		if o5 >= 1:
			o5 = 2*2
			o5 = o5-m6
			paths.append(1)
		else:
			m6 = 8*m6
			x = 9+x
			paths.append(2)
		if o5 < 7:
			m6 = 9-5
			paths.append(3)
		else:
			o5 = x/m6
			o5 = 0+o5
			x = 9/x
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		x = o5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))