import numpy as np 

def function(x):

	f9 = 3
	o1 = x
	paths = []
	try:
		if f9 > 7:
			x = x*6
			paths.append(1)
		else:
			x = 1-x
			x = 4-x
			f9 = f9/4
			paths.append(2)
		if f9 >= 7:
			f9 = f9*2
			paths.append(3)
		else:
			o1 = o1+3
			f9 = f9*7
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		f9 = o1**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))