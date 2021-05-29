import numpy as np 

def function(x):

	f8 = x
	r3 = x
	paths = []
	try:
		if x >= 7:
			r3 = x*5
			x = x+x
			x = x-2
			paths.append(1)
		else:
			r3 = 6+r3
			paths.append(2)
		if r3 >= 3:
			x = f8+4
			r3 = r3+3
			paths.append(3)
		else:
			r3 = r3+5
			x = 6+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f8 = x**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))