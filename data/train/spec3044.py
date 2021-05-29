import numpy as np 

def function(x):

	j4 = 0
	b5 = 4
	paths = []
	try:
		if b5 > 8:
			j4 = j4*7
			b5 = b5*7
			paths.append(1)
		else:
			j4 = x-1
			b5 = 0*6
			paths.append(2)
		if x <= 0:
			x = x/9
			paths.append(3)
		else:
			x = 7-3
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		b5 = j4**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))