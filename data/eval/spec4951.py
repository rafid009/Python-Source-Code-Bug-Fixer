import numpy as np 

def function(x):

	d7 = x
	i3 = x
	paths = []
	try:
		if d7 < 7:
			d7 = 9+x
			x = 7/d7
			i3 = 6*i3
			paths.append(1)
		else:
			i3 = 6-i3
			paths.append(2)
		if x < 4:
			x = 2*x
			paths.append(3)
		else:
			i3 = x*8
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