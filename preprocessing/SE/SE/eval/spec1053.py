import numpy as np 

def function(x):

	r1 = x
	w2 = x
	paths = []
	try:
		if r1 > 4:
			x = x+r1
			r1 = 8-r1
			r1 = 2+r1
			paths.append(1)
		else:
			r1 = 2-4
			paths.append(2)
		if r1 < 8:
			r1 = r1*x
			x = x-7
			r1 = r1/4
			paths.append(3)
		else:
			w2 = w2+9
			r1 = w2*r1
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		r1 = w2**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))