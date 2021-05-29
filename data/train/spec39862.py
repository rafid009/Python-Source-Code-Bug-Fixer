import numpy as np 

def function(x):

	d7 = x
	b6 = 9
	paths = []
	try:
		if x < 8:
			b6 = b6-x
			b6 = 5/6
			paths.append(1)
		else:
			x = x*2
			x = x/8
			paths.append(2)
		if d7 < 9:
			d7 = 4+d7
			d7 = b6*x
			b6 = b6*0
			paths.append(3)
		else:
			b6 = 8+b6
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