import numpy as np 

def function(x):

	w5 = x
	u3 = x
	x = 9
	paths = []
	try:
		if w5 >= 0:
			x = x+5
			w5 = w5-6
			x = 5+x
			paths.append(1)
		else:
			x = 5*1
			w5 = x/u3
			u3 = u3+0
			paths.append(2)
		if w5 >= 9:
			x = 2*x
			w5 = 7/u3
			paths.append(3)
		else:
			w5 = 8-7
			w5 = w5-7
			x = x*4
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		w5 = w5**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))