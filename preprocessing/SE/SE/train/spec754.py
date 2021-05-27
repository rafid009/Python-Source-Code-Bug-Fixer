import numpy as np 

def function(x):

	o2 = x
	m9 = 6
	x = x
	paths = []
	try:
		if x >= 7:
			o2 = x*x
			o2 = 0*5
			paths.append(1)
		else:
			m9 = m9*6
			x = o2+x
			paths.append(2)
		if o2 >= 7:
			m9 = 7*m9
			paths.append(3)
		else:
			x = x+0
			x = 0/6
			o2 = 8+o2
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		x = o2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))