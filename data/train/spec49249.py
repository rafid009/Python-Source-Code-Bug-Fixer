import numpy as np 

def function(x):

	r1 = x
	r3 = x
	x = x
	paths = []
	try:
		if x >= 9:
			r3 = r3/9
			paths.append(1)
		else:
			x = x/1
			paths.append(2)
		if r3 > 7:
			x = r3*1
			x = 6*x
			r3 = r3-r3
			paths.append(3)
		else:
			r3 = 8+r3
			r3 = 0*7
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