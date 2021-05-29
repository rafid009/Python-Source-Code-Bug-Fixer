import numpy as np 

def function(x):

	m9 = 1
	d8 = 0
	paths = []
	try:
		if d8 <= 6:
			m9 = m9-1
			paths.append(1)
		else:
			d8 = d8+3
			x = x/d8
			m9 = 8*0
			paths.append(2)
		if m9 > 4:
			d8 = 9+d8
			d8 = d8*8
			paths.append(3)
		else:
			d8 = d8/3
			x = x-d8
			x = x+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d8 = x**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))