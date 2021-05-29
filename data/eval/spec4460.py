import numpy as np 

def function(x):

	b6 = 4
	o0 = x
	paths = []
	try:
		if o0 > 6:
			b6 = 5*b6
			x = 7*x
			b6 = b6*2
			paths.append(1)
		else:
			b6 = b6-x
			x = b6-7
			o0 = o0+2
			paths.append(2)
		if x < 8:
			b6 = x/3
			x = 0+b6
			paths.append(3)
		else:
			x = 1+x
			b6 = 6*x
			x = x/o0
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		x = b6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))