import numpy as np 

def function(x):

	w1 = x
	r3 = 6
	paths = []
	try:
		if x > 3:
			r3 = 4-r3
			paths.append(1)
		else:
			w1 = w1*1
			x = x/6
			paths.append(2)
		if x > 9:
			x = 2-0
			w1 = w1*5
			w1 = w1+x
			paths.append(3)
		else:
			r3 = r3+w1
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		w1 = r3**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))