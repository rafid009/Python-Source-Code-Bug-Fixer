import numpy as np 

def function(x):

	r5 = x
	b4 = 6
	paths = []
	try:
		if r5 > 1:
			r5 = x*r5
			b4 = 8+4
			x = x*1
			paths.append(1)
		else:
			b4 = 2/x
			r5 = 0/1
			x = x+x
			paths.append(2)
		if r5 >= 4:
			b4 = b4*b4
			r5 = 5-r5
			x = 4-x
			paths.append(3)
		else:
			x = x+6
			x = x/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b4 = x**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))