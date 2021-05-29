import numpy as np 

def function(x):

	w2 = x
	d3 = x
	paths = []
	try:
		if x > 4:
			w2 = w2*w2
			paths.append(1)
		else:
			w2 = w2*8
			paths.append(2)
		if w2 <= 2:
			w2 = w2/5
			w2 = 6*w2
			d3 = 3+d3
			paths.append(3)
		else:
			w2 = w2+9
			d3 = d3/d3
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