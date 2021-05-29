import numpy as np 

def function(x):

	b3 = x
	o2 = 7
	x = x
	paths = []
	try:
		if b3 > 1:
			b3 = 3-1
			paths.append(1)
		else:
			x = o2*x
			x = x*5
			x = 2+x
			paths.append(2)
		if b3 < 1:
			o2 = 3+9
			b3 = b3/6
			paths.append(3)
		else:
			o2 = 9/6
			b3 = b3+8
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		o2 = b3**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))