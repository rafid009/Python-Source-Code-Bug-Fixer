import numpy as np 

def function(x):

	b5 = x
	r5 = x
	paths = []
	try:
		if b5 > 7:
			b5 = r5/b5
			r5 = r5+0
			x = x*5
			paths.append(1)
		else:
			r5 = 0*r5
			r5 = b5+r5
			b5 = 5/b5
			paths.append(2)
		if b5 < 9:
			b5 = b5-x
			x = x/9
			paths.append(3)
		else:
			r5 = 8-r5
			x = 6*6
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		x = b5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))