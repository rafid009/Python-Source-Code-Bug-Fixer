import numpy as np 

def function(x):

	r6 = 6
	w1 = x
	x = x
	paths = []
	try:
		if x > 8:
			r6 = r6-8
			r6 = 9+r6
			x = x-4
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if w1 < 5:
			w1 = 7*w1
			r6 = r6*6
			r6 = 2*1
			paths.append(3)
		else:
			r6 = r6-5
			r6 = r6+4
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		r6 = w1**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))