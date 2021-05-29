import numpy as np 

def function(x):

	r3 = 9
	w5 = x
	paths = []
	try:
		if w5 < 4:
			r3 = r3/r3
			paths.append(1)
		else:
			x = x-0
			r3 = w5-r3
			r3 = x*0
			paths.append(2)
		if w5 <= 1:
			x = x-3
			w5 = 4+x
			paths.append(3)
		else:
			w5 = 0/w5
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		x = w5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))