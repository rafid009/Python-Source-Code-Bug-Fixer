import numpy as np 

def function(x):

	j8 = 0
	w2 = 5
	paths = []
	try:
		if j8 >= 0:
			j8 = 7/x
			w2 = j8*2
			j8 = j8/w2
			paths.append(1)
		else:
			w2 = 8/2
			w2 = w2*3
			paths.append(2)
		if x >= 0:
			x = 4+x
			w2 = w2+3
			j8 = j8*2
			paths.append(3)
		else:
			x = 4/4
			w2 = x-x
			w2 = j8-6
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		w2 = w2**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))