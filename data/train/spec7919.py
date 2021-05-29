import numpy as np 

def function(x):

	b0 = x
	x6 = x
	paths = []
	try:
		if x6 < 1:
			x6 = x6+x
			b0 = 7*6
			b0 = b0*0
			paths.append(1)
		else:
			x6 = 4*b0
			b0 = x6-6
			paths.append(2)
		if x6 <= 8:
			x6 = x6*x6
			paths.append(3)
		else:
			x = 5*x
			x6 = x6-9
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		x6 = b0**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))