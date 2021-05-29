import numpy as np 

def function(x):

	w2 = x
	t4 = 8
	paths = []
	try:
		if w2 < 4:
			w2 = w2/4
			x = 3-5
			w2 = 4*w2
			paths.append(1)
		else:
			t4 = 3/9
			paths.append(2)
		if t4 <= 0:
			x = x-t4
			x = 6/x
			w2 = w2+5
			paths.append(3)
		else:
			w2 = w2+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t4 = x**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))