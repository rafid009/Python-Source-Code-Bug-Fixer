import numpy as np 

def function(x):

	r5 = 5
	a0 = x
	paths = []
	try:
		if x >= 8:
			r5 = r5*6
			paths.append(1)
		else:
			r5 = r5*0
			r5 = x-1
			paths.append(2)
		if x > 5:
			x = r5-2
			r5 = r5+1
			paths.append(3)
		else:
			x = a0*9
			a0 = a0+0
			x = x+2
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		x = a0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))