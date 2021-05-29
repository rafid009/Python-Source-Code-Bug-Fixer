import numpy as np 

def function(x):

	m4 = 2
	o8 = 2
	paths = []
	try:
		if m4 > 2:
			o8 = o8*9
			paths.append(1)
		else:
			x = o8-x
			o8 = o8+1
			paths.append(2)
		if o8 > 4:
			o8 = 4/o8
			o8 = m4/o8
			x = m4/9
			paths.append(3)
		else:
			o8 = m4*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m4 = x**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))