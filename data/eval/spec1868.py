import numpy as np 

def function(x):

	w1 = x
	t1 = x
	paths = []
	try:
		if x >= 4:
			w1 = x/w1
			x = x+7
			t1 = 3-t1
			paths.append(1)
		else:
			w1 = t1/3
			w1 = w1*4
			w1 = 5+7
			paths.append(2)
		if t1 > 1:
			w1 = w1/w1
			x = x*2
			paths.append(3)
		else:
			t1 = 2/t1
			w1 = 4-w1
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