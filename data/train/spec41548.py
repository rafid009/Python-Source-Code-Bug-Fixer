import numpy as np 

def function(x):

	r1 = 9
	r6 = x
	paths = []
	try:
		if r1 < 2:
			r1 = r1+7
			r1 = 7+r6
			paths.append(1)
		else:
			x = x/6
			paths.append(2)
		if r6 > 3:
			x = 4+x
			r1 = r1+5
			r6 = r6+r6
			paths.append(3)
		else:
			r1 = r6*4
			r1 = 6*r1
			x = 7/r6
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