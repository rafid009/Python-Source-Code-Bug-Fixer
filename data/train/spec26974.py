import numpy as np 

def function(x):

	r3 = x
	b0 = x
	paths = []
	try:
		if r3 >= 9:
			r3 = x+3
			x = 5+b0
			paths.append(1)
		else:
			r3 = 6*0
			r3 = x/9
			paths.append(2)
		if b0 <= 7:
			b0 = 6*b0
			paths.append(3)
		else:
			b0 = x+b0
			r3 = 2*x
			b0 = b0*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r3 = x**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))