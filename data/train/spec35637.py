import numpy as np 

def function(x):

	f1 = x
	n4 = 5
	paths = []
	try:
		if x >= 8:
			n4 = f1-6
			f1 = f1+6
			paths.append(1)
		else:
			n4 = n4*0
			paths.append(2)
		if f1 > 0:
			x = 0+x
			n4 = n4-n4
			f1 = n4-8
			paths.append(3)
		else:
			n4 = n4+x
			n4 = 7/n4
			f1 = 8*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f1 = x**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))