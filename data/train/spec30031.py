import numpy as np 

def function(x):

	o8 = 8
	r8 = 8
	paths = []
	try:
		if x <= 9:
			r8 = r8-8
			paths.append(1)
		else:
			o8 = o8/o8
			r8 = 5-x
			paths.append(2)
		if r8 <= 2:
			r8 = x+0
			x = 2-x
			paths.append(3)
		else:
			r8 = 3+r8
			o8 = o8-6
			r8 = x-1
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		x = r8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))