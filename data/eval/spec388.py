import numpy as np 

def function(x):

	m4 = x
	x8 = x
	paths = []
	try:
		if m4 >= 3:
			x = x*3
			paths.append(1)
		else:
			x8 = 2/6
			x8 = x*0
			x8 = 9+x8
			paths.append(2)
		if m4 <= 8:
			x8 = x8+4
			m4 = m4-7
			paths.append(3)
		else:
			x8 = x8-m4
			m4 = 0+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x8 = x**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))