import numpy as np 

def function(x):

	b2 = 2
	n5 = 4
	paths = []
	try:
		if n5 >= 6:
			b2 = b2-7
			b2 = 2*x
			b2 = n5+b2
			paths.append(1)
		else:
			x = x*n5
			n5 = 6+b2
			b2 = b2*6
			paths.append(2)
		if x <= 8:
			n5 = n5*0
			paths.append(3)
		else:
			x = 5*x
			b2 = x-b2
			n5 = 2-6
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		b2 = n5**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))