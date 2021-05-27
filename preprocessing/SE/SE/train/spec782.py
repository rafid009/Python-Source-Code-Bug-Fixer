import numpy as np 

def function(x):

	r8 = 3
	o9 = 0
	paths = []
	try:
		if r8 <= 1:
			r8 = 0+r8
			r8 = r8*5
			paths.append(1)
		else:
			x = 7/x
			r8 = 6+3
			r8 = r8/x
			paths.append(2)
		if r8 <= 9:
			o9 = o9/7
			x = x+r8
			paths.append(3)
		else:
			o9 = x+o9
			r8 = r8/x
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