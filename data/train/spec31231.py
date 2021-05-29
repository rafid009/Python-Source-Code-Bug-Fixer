import numpy as np 

def function(x):

	f2 = 8
	k7 = x
	paths = []
	try:
		if x <= 8:
			x = f2-x
			f2 = 7/f2
			x = x-f2
			paths.append(1)
		else:
			x = x+f2
			paths.append(2)
		if k7 < 4:
			x = x/5
			k7 = 1*f2
			paths.append(3)
		else:
			x = x-8
			x = 3+x
			x = x/f2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f2 = x**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))