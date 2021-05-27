import numpy as np 

def function(x):

	f9 = 8
	n4 = x
	paths = []
	try:
		if x >= 3:
			n4 = n4/2
			f9 = 0*0
			paths.append(1)
		else:
			x = x*4
			paths.append(2)
		if f9 < 0:
			f9 = f9/f9
			n4 = n4+8
			n4 = 4/1
			paths.append(3)
		else:
			x = x+9
			n4 = 3*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n4 = x**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))