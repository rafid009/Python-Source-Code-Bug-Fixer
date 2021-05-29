import numpy as np 

def function(x):

	t3 = 1
	w2 = x
	paths = []
	try:
		if t3 >= 1:
			x = 9/x
			paths.append(1)
		else:
			x = w2+t3
			x = 4-4
			paths.append(2)
		if w2 < 6:
			w2 = w2*3
			w2 = x+5
			t3 = 1-t3
			paths.append(3)
		else:
			t3 = t3/t3
			w2 = w2-0
			t3 = t3+9
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