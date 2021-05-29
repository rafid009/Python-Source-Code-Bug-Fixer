import numpy as np 

def function(x):

	d2 = 1
	x8 = x
	paths = []
	try:
		if x <= 5:
			x8 = d2*0
			d2 = 1*2
			x = 1+x
			paths.append(1)
		else:
			x = x*4
			paths.append(2)
		if x8 <= 9:
			x8 = x8-d2
			paths.append(3)
		else:
			x8 = 4+x8
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		x = x8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))