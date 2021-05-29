import numpy as np 

def function(x):

	b0 = 3
	r5 = x
	paths = []
	try:
		if b0 > 1:
			b0 = b0-4
			x = b0-6
			paths.append(1)
		else:
			b0 = 6/b0
			b0 = x/b0
			r5 = x*r5
			paths.append(2)
		if x <= 9:
			x = x*b0
			paths.append(3)
		else:
			x = 9/9
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		b0 = r5**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))