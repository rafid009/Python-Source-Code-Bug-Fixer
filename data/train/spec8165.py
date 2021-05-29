import numpy as np 

def function(x):

	f5 = 1
	o7 = x
	paths = []
	try:
		if x > 4:
			x = x*4
			o7 = 0*3
			f5 = o7+0
			paths.append(1)
		else:
			o7 = x+7
			f5 = 9+3
			paths.append(2)
		if f5 >= 9:
			o7 = 9+x
			paths.append(3)
		else:
			o7 = 1+o7
			f5 = x/o7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f5 = x**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))