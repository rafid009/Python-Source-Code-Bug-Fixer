import numpy as np 

def function(x):

	j9 = 3
	w5 = 9
	paths = []
	try:
		if x > 4:
			x = x/1
			w5 = x-w5
			x = x/j9
			paths.append(1)
		else:
			w5 = w5/9
			paths.append(2)
		if j9 >= 6:
			w5 = 8+1
			paths.append(3)
		else:
			w5 = w5+8
			w5 = 3*0
			w5 = x/j9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j9 = x**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))