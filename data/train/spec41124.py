import numpy as np 

def function(x):

	w1 = x
	f2 = x
	paths = []
	try:
		if f2 >= 8:
			w1 = w1-5
			x = w1/x
			f2 = 5/3
			paths.append(1)
		else:
			w1 = w1+8
			paths.append(2)
		if f2 <= 1:
			f2 = f2/9
			f2 = 0+8
			paths.append(3)
		else:
			f2 = 2-f2
			w1 = w1/2
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		f2 = w1**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))