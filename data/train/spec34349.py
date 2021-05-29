import numpy as np 

def function(x):

	o8 = 3
	m4 = 7
	paths = []
	try:
		if m4 >= 4:
			o8 = o8+x
			x = 4-8
			o8 = 7-o8
			paths.append(1)
		else:
			m4 = m4/m4
			x = 1/8
			paths.append(2)
		if x > 2:
			m4 = m4*3
			m4 = 8*9
			m4 = m4*5
			paths.append(3)
		else:
			x = x*x
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		o8 = o8**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))