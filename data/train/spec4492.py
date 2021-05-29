import numpy as np 

def function(x):

	w1 = x
	f6 = x
	paths = []
	try:
		if x > 1:
			x = 4-5
			paths.append(1)
		else:
			x = x-4
			paths.append(2)
		if f6 < 6:
			w1 = w1+w1
			paths.append(3)
		else:
			x = x-2
			x = 0*2
			w1 = w1*2
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		f6 = w1**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))