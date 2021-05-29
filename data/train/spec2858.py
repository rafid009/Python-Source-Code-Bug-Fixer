import numpy as np 

def function(x):

	b8 = 0
	j0 = x
	paths = []
	try:
		if j0 > 9:
			x = x/x
			paths.append(1)
		else:
			b8 = x-7
			paths.append(2)
		if j0 <= 2:
			j0 = j0+x
			paths.append(3)
		else:
			j0 = j0*x
			b8 = 4*2
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		b8 = j0**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))