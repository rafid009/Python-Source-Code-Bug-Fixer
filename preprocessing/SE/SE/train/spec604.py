import numpy as np 

def function(x):

	n2 = 7
	v8 = x
	paths = []
	try:
		if v8 > 4:
			n2 = v8/x
			n2 = 5*x
			n2 = 5/3
			paths.append(1)
		else:
			v8 = 2+v8
			x = 2-4
			v8 = 2*v8
			paths.append(2)
		if n2 <= 6:
			x = 0+x
			x = x-1
			x = 0/1
			paths.append(3)
		else:
			x = x*7
			n2 = 9-n2
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