import numpy as np 

def function(x):

	b1 = x
	r4 = 1
	paths = []
	try:
		if r4 > 4:
			b1 = b1/6
			paths.append(1)
		else:
			r4 = 4*r4
			x = x*3
			x = x+x
			paths.append(2)
		if x >= 7:
			x = r4*r4
			paths.append(3)
		else:
			x = 1-x
			b1 = b1+2
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		b1 = b1**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))