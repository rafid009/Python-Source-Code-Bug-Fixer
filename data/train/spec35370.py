import numpy as np 

def function(x):

	w6 = x
	i2 = 3
	paths = []
	try:
		if w6 < 7:
			x = 6+x
			i2 = w6*7
			w6 = w6/8
			paths.append(1)
		else:
			x = x-9
			x = i2-8
			w6 = i2/w6
			paths.append(2)
		if x >= 3:
			i2 = i2*4
			i2 = i2-w6
			paths.append(3)
		else:
			x = x*3
			x = i2+8
			i2 = 0*i2
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