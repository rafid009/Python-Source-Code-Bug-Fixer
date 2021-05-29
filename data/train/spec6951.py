import numpy as np 

def function(x):

	f4 = x
	o1 = x
	x = x
	paths = []
	try:
		if f4 >= 3:
			x = x+1
			x = x-3
			paths.append(1)
		else:
			f4 = 2-1
			o1 = x-o1
			o1 = o1+3
			paths.append(2)
		if f4 < 2:
			f4 = 1+f4
			o1 = o1+7
			paths.append(3)
		else:
			f4 = 8+7
			o1 = x+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f4 = x**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))