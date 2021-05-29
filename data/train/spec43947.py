import numpy as np 

def function(x):

	i7 = x
	m2 = 7
	paths = []
	try:
		if x <= 7:
			i7 = 4/5
			i7 = 8+i7
			paths.append(1)
		else:
			m2 = 9/m2
			i7 = 4-i7
			paths.append(2)
		if m2 < 4:
			i7 = i7+6
			paths.append(3)
		else:
			i7 = i7-5
			x = x+1
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