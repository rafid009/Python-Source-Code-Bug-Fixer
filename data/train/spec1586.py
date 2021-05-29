import numpy as np 

def function(x):

	x9 = x
	f9 = x
	paths = []
	try:
		if x > 7:
			x = x+5
			paths.append(1)
		else:
			f9 = f9/6
			x = 4/x
			x9 = x/9
			paths.append(2)
		if x <= 0:
			x = 8+x
			paths.append(3)
		else:
			f9 = x9/f9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f9 = x**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))