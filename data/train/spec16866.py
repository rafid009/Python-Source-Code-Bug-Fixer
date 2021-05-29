import numpy as np 

def function(x):

	r1 = 0
	w1 = 0
	paths = []
	try:
		if w1 >= 2:
			x = r1-0
			paths.append(1)
		else:
			r1 = x/x
			w1 = 5+w1
			paths.append(2)
		if r1 > 7:
			w1 = w1/x
			w1 = 0/w1
			paths.append(3)
		else:
			r1 = r1/2
			r1 = x*7
			x = w1*r1
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		r1 = r1**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))