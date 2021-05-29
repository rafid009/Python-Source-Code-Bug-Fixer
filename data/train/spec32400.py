import numpy as np 

def function(x):

	j7 = x
	w5 = 3
	paths = []
	try:
		if j7 <= 4:
			w5 = w5*x
			w5 = 9*2
			paths.append(1)
		else:
			w5 = w5-8
			j7 = 7/w5
			j7 = 9/1
			paths.append(2)
		if j7 < 9:
			w5 = w5*j7
			paths.append(3)
		else:
			x = 6/x
			x = x-0
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		j7 = w5**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))