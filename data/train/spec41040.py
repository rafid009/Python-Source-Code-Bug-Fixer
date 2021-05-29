import numpy as np 

def function(x):

	f2 = x
	w9 = x
	x = x
	paths = []
	try:
		if w9 <= 1:
			x = f2-x
			f2 = 8/f2
			paths.append(1)
		else:
			w9 = w9/x
			paths.append(2)
		if w9 > 8:
			x = f2*1
			w9 = 7/w9
			paths.append(3)
		else:
			x = x/3
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		f2 = w9**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))