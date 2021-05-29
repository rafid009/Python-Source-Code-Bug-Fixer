import numpy as np 

def function(x):

	w1 = x
	r6 = x
	paths = []
	try:
		if x < 2:
			x = 4-1
			x = x+x
			paths.append(1)
		else:
			r6 = w1/r6
			paths.append(2)
		if r6 < 3:
			w1 = x*x
			r6 = r6+r6
			w1 = w1-3
			paths.append(3)
		else:
			w1 = 7*6
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		w1 = r6**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))