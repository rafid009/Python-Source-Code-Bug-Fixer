import numpy as np 

def function(x):

	x8 = x
	r1 = x
	paths = []
	try:
		if r1 >= 5:
			r1 = 8/8
			paths.append(1)
		else:
			r1 = r1+0
			x8 = 0-x8
			r1 = r1*5
			paths.append(2)
		if r1 >= 8:
			x8 = x*8
			r1 = r1/x8
			paths.append(3)
		else:
			x = x/6
			x = x+9
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		x = r1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))