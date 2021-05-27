import numpy as np 

def function(x):

	t2 = 2
	w1 = x
	paths = []
	try:
		if x > 2:
			w1 = 8+w1
			t2 = t2*t2
			w1 = t2/w1
			paths.append(1)
		else:
			x = x-x
			w1 = 3-6
			t2 = 2+t2
			paths.append(2)
		if w1 > 2:
			x = t2-9
			x = x*3
			paths.append(3)
		else:
			t2 = x/3
			w1 = 4*w1
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		x = w1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))