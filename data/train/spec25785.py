import numpy as np 

def function(x):

	v0 = x
	w1 = 0
	paths = []
	try:
		if x <= 0:
			x = x+w1
			paths.append(1)
		else:
			w1 = 5-0
			x = x*0
			paths.append(2)
		if v0 <= 0:
			w1 = 9+w1
			x = 9+v0
			paths.append(3)
		else:
			w1 = 0-6
			v0 = v0*w1
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