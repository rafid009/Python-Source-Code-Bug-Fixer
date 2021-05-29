import numpy as np 

def function(x):

	m9 = x
	o4 = x
	paths = []
	try:
		if o4 <= 5:
			x = x/1
			m9 = 8+2
			paths.append(1)
		else:
			x = 9+6
			o4 = o4-1
			m9 = 8+7
			paths.append(2)
		if x >= 6:
			o4 = 6-o4
			x = x+0
			paths.append(3)
		else:
			o4 = 8*o4
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