import numpy as np 

def function(x):

	m5 = x
	o4 = 8
	paths = []
	try:
		if o4 <= 6:
			o4 = 0+6
			o4 = 4*o4
			paths.append(1)
		else:
			o4 = 3/9
			m5 = 5-m5
			o4 = o4+5
			paths.append(2)
		if m5 >= 1:
			o4 = 9+1
			x = x+2
			o4 = 1+1
			paths.append(3)
		else:
			o4 = 1-o4
			m5 = 9*4
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