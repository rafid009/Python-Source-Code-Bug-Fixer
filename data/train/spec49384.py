import numpy as np 

def function(x):

	w6 = 0
	a3 = x
	paths = []
	try:
		if w6 > 9:
			w6 = x*a3
			a3 = a3/2
			paths.append(1)
		else:
			a3 = a3-0
			w6 = 4*w6
			paths.append(2)
		if w6 <= 1:
			w6 = w6+8
			paths.append(3)
		else:
			w6 = 0*4
			x = x/w6
			a3 = a3*8
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		a3 = a3**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))