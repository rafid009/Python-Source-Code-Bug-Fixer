import numpy as np 

def function(x):

	f3 = 6
	r8 = 2
	paths = []
	try:
		if x > 7:
			x = x+6
			paths.append(1)
		else:
			r8 = f3-7
			x = r8*5
			f3 = 3/9
			paths.append(2)
		if f3 < 4:
			f3 = f3-f3
			f3 = f3/7
			r8 = 8*5
			paths.append(3)
		else:
			x = r8+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r8 = x**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))