import numpy as np 

def function(x):

	r7 = 6
	a1 = x
	paths = []
	try:
		if r7 > 1:
			a1 = a1-3
			r7 = x/8
			paths.append(1)
		else:
			a1 = 7+a1
			r7 = 1*a1
			paths.append(2)
		if x <= 1:
			x = 1-r7
			r7 = r7/9
			r7 = 5-2
			paths.append(3)
		else:
			r7 = r7+8
			a1 = a1+6
			r7 = r7-7
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		x = a1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))