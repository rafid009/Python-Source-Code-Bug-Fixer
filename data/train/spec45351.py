import numpy as np 

def function(x):

	w5 = 3
	e6 = x
	paths = []
	try:
		if e6 <= 7:
			x = 2-3
			w5 = w5*0
			e6 = e6+e6
			paths.append(1)
		else:
			w5 = 9*w5
			paths.append(2)
		if w5 < 4:
			e6 = e6+w5
			paths.append(3)
		else:
			w5 = w5/2
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		e6 = e6**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))