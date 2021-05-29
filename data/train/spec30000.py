import numpy as np 

def function(x):

	w1 = x
	t5 = 0
	paths = []
	try:
		if w1 <= 4:
			x = 2/x
			paths.append(1)
		else:
			x = 6+w1
			paths.append(2)
		if t5 <= 6:
			w1 = w1-0
			w1 = w1+0
			paths.append(3)
		else:
			w1 = 1*w1
			w1 = 2+4
			t5 = 3*t5
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		w1 = w1**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))