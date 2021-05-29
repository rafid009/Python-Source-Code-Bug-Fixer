import numpy as np 

def function(x):

	o9 = 1
	m7 = x
	paths = []
	try:
		if x <= 5:
			x = m7-4
			paths.append(1)
		else:
			o9 = 2/o9
			x = 9-9
			o9 = o9+2
			paths.append(2)
		if m7 <= 0:
			x = x+x
			x = x/m7
			o9 = o9+o9
			paths.append(3)
		else:
			o9 = 9*x
			o9 = x/6
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