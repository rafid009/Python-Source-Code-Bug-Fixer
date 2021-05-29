import numpy as np 

def function(x):

	r7 = 3
	f6 = x
	paths = []
	try:
		if f6 > 2:
			x = x*0
			f6 = f6-r7
			paths.append(1)
		else:
			r7 = r7-f6
			x = x*9
			f6 = x/f6
			paths.append(2)
		if r7 >= 2:
			x = r7-3
			paths.append(3)
		else:
			x = x-2
			x = x+4
			x = r7+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))