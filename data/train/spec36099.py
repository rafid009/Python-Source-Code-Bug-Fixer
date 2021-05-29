import numpy as np 

def function(x):

	n2 = x
	f2 = 5
	paths = []
	try:
		if f2 < 0:
			n2 = f2/1
			paths.append(1)
		else:
			n2 = x*7
			x = 7-8
			f2 = 3+x
			paths.append(2)
		if x < 4:
			f2 = f2+2
			n2 = n2+n2
			n2 = 5*8
			paths.append(3)
		else:
			n2 = n2-6
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