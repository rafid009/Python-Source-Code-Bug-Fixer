import numpy as np 

def function(x):

	x6 = x
	b6 = x
	x = 2
	paths = []
	try:
		if x > 8:
			x = 6+x
			b6 = b6/9
			b6 = 8*x6
			paths.append(1)
		else:
			b6 = b6*x
			b6 = b6*b6
			b6 = 3*1
			paths.append(2)
		if b6 <= 7:
			x = x*5
			x = x6+x
			x = x/8
			paths.append(3)
		else:
			x = x*x
			x = x+0
			x = x*5
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x = x6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))