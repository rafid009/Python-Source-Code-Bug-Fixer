import numpy as np 

def function(x):

	w2 = x
	t3 = 1
	paths = []
	try:
		if x <= 7:
			t3 = x*t3
			w2 = w2+1
			t3 = x*8
			paths.append(1)
		else:
			w2 = t3/w2
			t3 = 2-9
			paths.append(2)
		if w2 > 4:
			w2 = w2*3
			w2 = 4-w2
			paths.append(3)
		else:
			x = x-0
			x = x-4
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		x = w2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))