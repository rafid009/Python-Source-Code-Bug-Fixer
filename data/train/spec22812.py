import numpy as np 

def function(x):

	m7 = x
	o9 = 4
	paths = []
	try:
		if x >= 6:
			o9 = 4/o9
			o9 = 9+o9
			paths.append(1)
		else:
			m7 = m7/8
			paths.append(2)
		if m7 < 0:
			x = 8*x
			o9 = 4/8
			o9 = o9+0
			paths.append(3)
		else:
			x = 0+1
			o9 = x/o9
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		x = m7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))