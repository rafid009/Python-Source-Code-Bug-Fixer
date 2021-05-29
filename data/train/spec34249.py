import numpy as np 

def function(x):

	o2 = x
	f5 = 8
	paths = []
	try:
		if x < 8:
			x = x*7
			x = 9/x
			paths.append(1)
		else:
			f5 = f5-f5
			paths.append(2)
		if f5 < 4:
			x = 6-1
			f5 = x-f5
			x = x+5
			paths.append(3)
		else:
			o2 = o2+o2
			f5 = f5*3
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