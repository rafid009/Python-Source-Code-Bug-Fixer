import numpy as np 

def function(x):

	q8 = 1
	m7 = 8
	paths = []
	try:
		if m7 < 4:
			x = 5+x
			x = q8*x
			paths.append(1)
		else:
			x = x*m7
			m7 = x+5
			paths.append(2)
		if m7 < 4:
			x = 8-1
			paths.append(3)
		else:
			x = q8-6
			x = x*2
			x = x+8
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