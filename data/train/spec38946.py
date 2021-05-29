import numpy as np 

def function(x):

	r8 = x
	r7 = 2
	paths = []
	try:
		if r7 <= 7:
			x = x*5
			r8 = 5*3
			r7 = 1+r7
			paths.append(1)
		else:
			x = r7-8
			x = x*r7
			paths.append(2)
		if x >= 5:
			x = 3-x
			paths.append(3)
		else:
			r8 = 1/r8
			r8 = x*8
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		x = r8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))