import numpy as np 

def function(x):

	f2 = 5
	w1 = 1
	paths = []
	try:
		if w1 > 7:
			x = x/6
			f2 = f2+6
			paths.append(1)
		else:
			w1 = w1+5
			x = 0*x
			paths.append(2)
		if x < 1:
			w1 = x-3
			x = 5-5
			paths.append(3)
		else:
			f2 = w1-8
			x = x-f2
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