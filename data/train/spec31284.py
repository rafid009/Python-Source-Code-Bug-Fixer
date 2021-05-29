import numpy as np 

def function(x):

	w1 = 5
	t4 = x
	paths = []
	try:
		if w1 >= 2:
			x = x/4
			w1 = 2/w1
			t4 = 4*0
			paths.append(1)
		else:
			t4 = t4/5
			x = x*3
			paths.append(2)
		if x >= 7:
			w1 = w1+w1
			paths.append(3)
		else:
			x = x/w1
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