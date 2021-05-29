import numpy as np 

def function(x):

	r5 = x
	a0 = 8
	paths = []
	try:
		if r5 <= 3:
			r5 = r5/2
			paths.append(1)
		else:
			r5 = r5+r5
			x = 5*1
			x = 9/6
			paths.append(2)
		if x > 2:
			x = x-6
			paths.append(3)
		else:
			a0 = 5+x
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		a0 = a0**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))