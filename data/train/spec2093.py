import numpy as np 

def function(x):

	u1 = 9
	w5 = x
	x = x
	paths = []
	try:
		if w5 < 4:
			w5 = w5*4
			u1 = 0+u1
			paths.append(1)
		else:
			w5 = w5+w5
			x = x*6
			u1 = u1+u1
			paths.append(2)
		if w5 > 9:
			x = 4+x
			x = w5-4
			paths.append(3)
		else:
			w5 = w5/3
			w5 = w5*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w5 = x**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))