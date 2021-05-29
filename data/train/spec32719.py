import numpy as np 

def function(x):

	f4 = 9
	n2 = x
	paths = []
	try:
		if f4 >= 2:
			f4 = x*f4
			paths.append(1)
		else:
			x = x+x
			x = x+4
			paths.append(2)
		if x <= 1:
			n2 = n2*0
			f4 = f4/3
			paths.append(3)
		else:
			n2 = f4+6
			f4 = 9*4
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		x = f4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))