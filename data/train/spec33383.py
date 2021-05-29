import numpy as np 

def function(x):

	o7 = x
	t7 = 8
	paths = []
	try:
		if t7 > 0:
			t7 = t7*2
			o7 = 0*o7
			x = x+6
			paths.append(1)
		else:
			o7 = 7-o7
			o7 = o7+1
			paths.append(2)
		if x > 4:
			o7 = 4*o7
			x = x*8
			paths.append(3)
		else:
			x = x+6
			o7 = o7-3
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