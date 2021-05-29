import numpy as np 

def function(x):

	j9 = 1
	o2 = 1
	paths = []
	try:
		if j9 < 7:
			j9 = j9*x
			o2 = o2+o2
			paths.append(1)
		else:
			j9 = 9*4
			j9 = 8+j9
			o2 = o2+6
			paths.append(2)
		if x > 6:
			x = x+3
			x = 4*9
			paths.append(3)
		else:
			o2 = o2*2
			o2 = o2/7
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