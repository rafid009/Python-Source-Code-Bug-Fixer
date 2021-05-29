import numpy as np 

def function(x):

	r3 = x
	o1 = x
	paths = []
	try:
		if r3 > 7:
			r3 = 7+8
			x = 7+6
			r3 = r3/3
			paths.append(1)
		else:
			o1 = o1-7
			paths.append(2)
		if o1 <= 0:
			x = o1+x
			paths.append(3)
		else:
			x = x/7
			r3 = r3*1
			x = x-6
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		x = o1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))