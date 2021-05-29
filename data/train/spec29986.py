import numpy as np 

def function(x):

	r6 = x
	r1 = 9
	paths = []
	try:
		if r1 > 3:
			r1 = 4*x
			r6 = 9-r6
			x = 2+x
			paths.append(1)
		else:
			x = 7*x
			x = x-0
			r6 = 6/r6
			paths.append(2)
		if r6 <= 6:
			x = x+4
			x = r6*2
			paths.append(3)
		else:
			r6 = r6-x
			r6 = 9+7
			r1 = r1*r1
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		x = r6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))