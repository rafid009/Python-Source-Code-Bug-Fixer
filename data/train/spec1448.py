import numpy as np 

def function(x):

	o8 = 0
	m7 = x
	paths = []
	try:
		if o8 <= 6:
			m7 = m7*1
			o8 = 1*x
			o8 = x*o8
			paths.append(1)
		else:
			o8 = m7*o8
			o8 = 0/6
			x = o8+o8
			paths.append(2)
		if x >= 2:
			o8 = x/1
			paths.append(3)
		else:
			x = x*9
			o8 = m7+o8
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