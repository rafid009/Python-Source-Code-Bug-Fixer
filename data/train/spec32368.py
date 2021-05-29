import numpy as np 

def function(x):

	o4 = x
	m8 = 3
	paths = []
	try:
		if o4 <= 2:
			o4 = 8*o4
			m8 = 6+3
			paths.append(1)
		else:
			x = x/1
			paths.append(2)
		if o4 > 1:
			x = 0+0
			x = x+4
			paths.append(3)
		else:
			x = 5*5
			x = x+3
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		x = o4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))