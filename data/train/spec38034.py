import numpy as np 

def function(x):

	j6 = x
	w5 = x
	paths = []
	try:
		if w5 > 0:
			j6 = 7/3
			x = 4*1
			paths.append(1)
		else:
			j6 = 4-2
			paths.append(2)
		if j6 < 3:
			x = x-j6
			x = x-7
			j6 = j6*3
			paths.append(3)
		else:
			w5 = 6+1
			j6 = j6-4
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