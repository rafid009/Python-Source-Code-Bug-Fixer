import numpy as np 

def function(x):

	w2 = x
	r5 = x
	x = 6
	paths = []
	try:
		if r5 <= 5:
			w2 = 5/w2
			x = w2-x
			x = 0*x
			paths.append(1)
		else:
			r5 = 8+r5
			paths.append(2)
		if x <= 8:
			x = x/1
			x = x*4
			w2 = w2/3
			paths.append(3)
		else:
			w2 = w2/3
			r5 = r5-7
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		r5 = w2**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))