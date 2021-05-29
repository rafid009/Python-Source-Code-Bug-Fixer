import numpy as np 

def function(x):

	o6 = 3
	m9 = x
	paths = []
	try:
		if m9 > 3:
			o6 = 8*m9
			m9 = m9/m9
			x = 9*x
			paths.append(1)
		else:
			o6 = o6/m9
			x = m9+o6
			o6 = o6-o6
			paths.append(2)
		if x <= 2:
			x = x-1
			o6 = 2*o6
			x = 1-m9
			paths.append(3)
		else:
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		x = m9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))