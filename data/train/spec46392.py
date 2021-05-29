import numpy as np 

def function(x):

	w8 = x
	r9 = x
	paths = []
	try:
		if w8 < 4:
			r9 = r9*0
			paths.append(1)
		else:
			r9 = r9*4
			x = 9-8
			paths.append(2)
		if r9 <= 8:
			r9 = 2*8
			x = x/4
			paths.append(3)
		else:
			w8 = w8+1
			x = 0+x
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		r9 = w8**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))