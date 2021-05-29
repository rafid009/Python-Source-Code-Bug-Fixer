import numpy as np 

def function(x):

	b7 = 1
	v8 = x
	paths = []
	try:
		if v8 <= 0:
			b7 = b7-2
			paths.append(1)
		else:
			x = x-8
			b7 = 1+b7
			b7 = 1/b7
			paths.append(2)
		if x <= 6:
			b7 = b7/3
			paths.append(3)
		else:
			v8 = 9*v8
			x = 3-v8
			v8 = b7*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v8 = x**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))