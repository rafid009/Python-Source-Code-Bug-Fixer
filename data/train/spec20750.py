import numpy as np 

def function(x):

	f0 = 6
	o0 = x
	paths = []
	try:
		if f0 < 3:
			f0 = f0/9
			x = 8-f0
			o0 = o0/7
			paths.append(1)
		else:
			o0 = 5/o0
			o0 = o0+8
			paths.append(2)
		if f0 >= 3:
			f0 = 9+x
			paths.append(3)
		else:
			f0 = f0/f0
			x = 5*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f0 = x**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))